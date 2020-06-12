import requests
import time
import threading
import urllib.parse
from queue import Queue
from core import config
import sys
# url = "http://testphp.vulnweb.com"
resume = None
proxies = {}
cookies = config.cookies
url = config.url
# wordlist_file ="../subdomains.txt"

number_threads = config.number_threads
wordlist_file = config.wordlist
extensions = config.extensions
raw_words = []
def build_wordlist(wordlist_file):
    # try:
    #     raw_words = open(wordlist_file,'r',errors="replace",encoding='utf-8').readlines()
    # except Exception as e:
    #     print(e)
    #     sys.exit(1)
    f = open(wordlist_file,"r")
    raw_word = f.readline()
    while raw_word != '':
        try:
            raw_word = f.readline()
            raw_words.append(raw_word)
        except:
            pass
    f.close()
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
        else:
            words.put(word)
    return words


def dirb(word_queue, extensions=None):
    while not word_queue.empty():
        attempt = word_queue.get()
        attempt_list = []
        if "." not in attempt:
            attempt_list.append("/%s/" % attempt)
        else:
            attempt_list.append("/%s/" % attempt)
        if extensions:
            for extension in extensions:
                attempt_list.append("/%s%s" % (attempt,extension))
        for brute in attempt_list:
            rq_url = "%s%s"%(url,brute)
            # print(rq_url)
            u = urllib.parse.urlparse(rq_url)
            u = u.geturl()
            # print(u.geturl())
            try:
                r = requests.get(u,proxies=proxies,cookies=cookies,allow_redirects =False)
                print("+ [%d] - %s"%(r.status_code,u))
            except Exception as e:
                print(e)
            
            # if r.status_code != 404:           
            #     print("+ [%d] - %s"%(r.status_code,u))

word_queue = build_wordlist(wordlist_file)

# while not word_queue.empty():
#     print(word_queue.get())

def main():
    for i in range(number_threads):
        t = threading.Thread(target=dirb,args=(word_queue,extensions,))
        t.start()