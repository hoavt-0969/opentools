import requests
import threading
from queue import Queue
import sys
import urllib
class Dirb(object):
    def __init__(self, url, extensions, wordlist, cookies=None, headers=None,threads=10,proxies=None):
        self.url = url
        self.extensions = extensions
        self.wordlist = wordlist
        self.cookies = cookies
        self.headers = headers
        self.threads = threads
        self.proxies = proxies
        self.resume = None
        self.words = Queue()
    
    def parse_cookie(self):
        if self.cookies == None:
            return self.cookies
        from http.cookies import SimpleCookie
        cookie = SimpleCookie()
        cookie.load(self.cookies)
        cookies = {}
        for key, data in cookie.items():
            cookies[key] = data.value
        return cookies
    def load_wordlist(self):
        try:
            raw_data = open(self.wordlist,'r',errors="replace").read().splitlines()
        except Exception as e:
            print(e)
            sys.exit(1)
        return raw_data
    
    def build_wordlist(self):
        found_resume = False
        raw_words = self.load_wordlist()
        # words = Queue()
        for word in raw_words:
            word = word.rstrip()
            if self.resume is not None:
                if found_resume:
                    self.words.put(word)
                else:
                    if word == self.resume:
                        found_resume = True
            else:
                self.words.put(word)
        
        return self.words

    def Scanner(self,word_queue):
        # print('hello')
        # print()
        while not word_queue.empty():
            attempt = word_queue.get()
            attempt_list = []
            if "." not in attempt:
                attempt_list.append("/%s/" %attempt)
            else:
                attempt_list.append("/%s/" %attempt)
            if self.extensions:
                for extension in self.extensions:
                    attempt_list.append("/%s%s"%(attempt,extension))
            for brute in attempt_list:
                url = "%s%s" %(self.url,brute)
                # print(brute)
                # print(url)
            
                try:
                    self.cookies = self.parse_cookie()
                    res = requests.get(url,cookies=self.cookies, allow_redirects=False, proxies=self.proxies)
                    if res.status_code !=404:
                        print("+ [%d] - %s"%(res.status_code,url))
                except Exception as e:
                    print("Error requests")
                # print(vars(res))
                # if res.status_code !=404:
                #     print("+ [%d] - %s"%(res.status_code,url))
        word_queue.task_done()

    def run(self):
        self.words = self.build_wordlist()
        # print(vars(self.build_wordlist()))
        for thread in range(self.threads):
            # t = threading.Thread(target=self.Scanner,args=(self.build_wordlist()))
            t = threading.Thread(target=self.Scanner,args=(self.words,))
            # print(t.getName)
            # t.daemon = True
            t.start()
            # t.join()