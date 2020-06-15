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
        # print(vars(self.build_wordlist()))
        for thread in range(self.threads):
            # t = threading.Thread(target=self.Scanner,args=(self.build_wordlist()))
            t = threading.Thread(target=self.Scanner,args=(self.build_wordlist(),))
            # t.daemon = True
            t.start()
            # t.join()

# def parse_args():
#     import argparse
#     parser = argparse.ArgumentParser(prog="scan")
#     subparsers = parser.add_subparsers(dest='command')

#     dirb_parser = subparsers.add_parser("dirb")
#     xss_parser = subparsers.add_parser("xss")
#     sub_parser = subparsers.add_parser("sub")

#     dirb_parser.add_argument('-u','--url',required=True,type=str,default=None)
#     dirb_parser.add_argument('-w','--wordlist',type=str,required=True,default="/home/sun/opentools/subdomains.txt")
#     dirb_parser.add_argument("-e","--extensions",type=str,required=True,default=".php,.html,.txt")
#     dirb_parser.add_argument("-t", "--threads",default=10,type=int,help="Set number threads", required=False)
#     dirb_parser.add_argument('--cookies', required=False,type=str)

#     xss_parser.add_argument('-u','--url',required=True,type=str)
#     xss_parser.add_argument('--cookies', required=False,type=str)

#     sub_parser.add_argument('-d', '--domain', required=True, type=str)
#     sub_parser.add_argument('-t', '--threads', required=False, type=int, default=10)
#     return parser.parse_args()



# if __name__ == "__main__":
#     # url = "http://testphp.vulnweb.com"
#     # threads = 100
#     # extensions = ['.php','.html','.txt']
#     # wordlist = "/usr/share/wordlists/dirb/big.txt"
#     # scanner = Dirb(url=url,extensions=extensions,wordlist=wordlist,threads=threads)
#     # scanner.run()
#     args = parse_args()
#     print(vars(args))
#     if args.command == "dirb":
#         if args.url[-1] == "/":
#             url = args.url[:-1]
#         else:
#             url = args.url
#     # print(url[-1])
#     # print(url)
#         threads = args.threads
#         cookies = parse_cookie(args.cookies)
#         wordlist = args.wordlist
#         extensions = args.extensions.split(",")
#         scanner = Dirb(url=url, extensions=extensions, wordlist=wordlist, threads=threads,cookies=cookies)
#         scanner.run()