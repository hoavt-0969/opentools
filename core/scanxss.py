import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import threading
from queue import Queue
from core import config
par = Queue()

url = config.url
params_fuzz = config.params_fuzz
payloads = config.payloads
number_threads = config.number_threads
proxies = config.proxies
def reflect_xss(url,params_fuzz):
    global par
    while not par.empty():
        param = par.get()
        # print(param)
        data = {param:payloads}
        res = requests.get(url=url, params=data,cookies=config.cookies, proxies=proxies,verify=False)
        if payloads in res.content.decode():
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Inputs details:")
            details = {
                "method":"get",
                "intpus":[{"param":param, "payload":payloads}]
            }
            pprint(details)
        par.task_done()

def scan_reflect(url,params_fuzz,number_threads):
    for param in params_fuzz:
        par.put(param)
    for i in range(number_threads):
        t = threading.Thread(target=reflect_xss,args=(url,params_fuzz,))
        t.daemon = True
        t.start()
def get_all_forms(url):
    soup = bs(requests.get(url,cookies=config.cookies).content,"html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    action = form.attrs.get("action")
    # print(action)
    method = form.attrs.get("method", "get")

    inputs = []
    all_form = form.find_all(["input", "textarea"])

    # all_form.append(form.find_all("input"))
    # print(all_form)
    for input_tag in all_form:
        # print(input_tag)
        input_type = input_tag.attrs.get("type","text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    # print(details["inputs"])
    return details

def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details['action'])

    inputs = form_details['inputs']

    data = {}
    for inp in inputs:
        if inp['type'] == "text" or inp['type'] == "search":
            inp['value'] = value
        input_name = inp.get("name")
        input_value = inp.get("value")
        if input_name and input_value:
            data[input_name] = input_value
    
    # print(data)
    if form_details["method"] == "post":
        #print(requests.post(target_url, data=data, cookies=cookies).content.decode())
        return requests.post(target_url, data=data, cookies=config.cookies,proxies=proxies,verify=False)
    else:
        return requests.get(target_url, params=data, cookies=config.cookies, proxies=proxies,verify=False)


def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    # payloads = 
    js_script = "<script>alert(\"tested\");</script>"
    is_vulnerable = False
    for form in forms:
        # print(form)
        form_details = get_form_details(form)
        print(form_details)
        content = submit_form(form_details, url, js_script).content.decode()
        # f = open("output.txt",'w')
        # f.write(content+"\n")
        # f.close()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable


def main():
    scan_reflect(url,params_fuzz,number_threads)
    scan_xss(url)
    par.join()