import urllib3
import threading
import requests
from queue import Queue

threads = 100

target_url = "http://testphp.vulnweb.com"
wordlist_file = "subdomains.txt"
resume = None
user_agent =  "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101¬Firefox/19.0"
proxies = {
    "https":"https://128.199.214.87:3128"
}
def build_wordlist(wordlist_file):
    fd = open(wordlist_file,"r")
    raw_words = fd.readlines()
    fd.close()
    found_resume = False
    words = Queue()
    for word in raw_words:
        word = word.rstrip()
        if resume is not None:
            if found_resume:
                words.put(word)
            else:
                if word == resume:
                    found_resume = True
                    print("Resuming wordlist form: ",resume)
        else:
            words.put(word)
    return words

# t = build_wordlist(wordlist_file)

# while not t.empty():
#     x = t.get()
#     print(x)
# print(build_wordlist(wordlist_file).qsize)
def dir_brute(word_queue, extensions=None):
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s/" %attempt)
        if extensions:
            for extension in extensions:
                attempt_list.append("/%s%s" % (attempt,extension) )
        for brute in attempt_list:
            url = "%s%s"%(target_url,brute)
            # print(url)
            r = requests.get(url,proxies=proxies)
            # r = requests.get(url)
            # if r.status_code != 404:
            print("[%d] => %s" %(r.status_code, url))
            # print(brute)
            # url = "%s%s" % (target_url,urllib3.quote(brute))
            # # try:
            # #     headers = {}
            # #     headers["User-Agent"] = user_agent
            # #     r = urllib3.Request(url)
            # #     res = urllib3.urlopen(r)
            # #     if len(res.read()):
            # #         print("[%d] => %s" %(res.code, url))
            # # except expression as identifier:
            # #     pass
    
word_queue = build_wordlist(wordlist_file)
extensions = [".php",".html",".txt",".inc",".bak"]
for i in range(threads):
    t = threading.Thread(target=dir_brute,args=(word_queue,extensions,))
    t.start()