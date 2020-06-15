# import requests
# import urllib3
# import sys
# import threading
# from core import config
# from queue import Queue

# d = Queue()

# def parse_url(url):
#     try:
#         host = urllib3.util.url.parse_url(url).host
#     except Exception as e:
#         print("Invalid domain, try again..")
#         sys.exit(1)
#     return host

# def parse_wordlist(wordlist):
#     try:
#         # print(wordlist)
#         wordlists = open(wordlist,'r',errors='replace',encoding='utf-8').read().splitlines()
#         # print(wordlists)
#     except Exception as e:
#         print(e)
#         sys.exit(1)
#     return wordlists
# def banner():
#     print('''
#  ____               ____ ____  ____  
# / ___| _   _ _ __  / ___/ ___||  _ \ 
# \___ \| | | | '_ \| |   \___ \| |_) |
#  ___) | |_| | | | | |___ ___) |  _ < 
# |____/ \__,_|_| |_|\____|____/|_| \_\ 
# =====================================
# ''')

# def scan_subdomain(target):
#     global d
#     while True:
#         subdomain = d.get()
#         url = f"http://{subdomain}.{target}"
#         try:
#             res = requests.get(url)
#         except Exception as e:
#             pass
#             # print("Error request")
#         #     pass
#         else:
#             print("[+] - %s - %d"%(url,res.status_code))
#         d.task_done()

# def mutil_scan_subdomains(target,number_threads,subdomains):
#     for subdomain in subdomains:
#         d.put(subdomain)
#     for thread in range(number_threads):
#         t = threading.Thread(target=scan_subdomain, args=(target,))
#         t.daemon = True
#         t.start()
# def main():
#     target = parse_url(config.domain)
#     wordlist = '/usr/share/wordlists/dirb/big.txt'
#     number_threads = config.threads
#     print("=====================")
#     mutil_scan_subdomains(target=target, number_threads=number_threads,subdomains=parse_wordlist(wordlist))
#     d.join()

import requests
import urllib3
import sys
import threading
from queue import Queue

class Sub(object):
    def __init__(self, domain, wordlist,threads = 10):
        self.domain = domain
        self.wordlist = wordlist
        self.word_queue = Queue()
        self.threads = threads
    def parse_url(self):
        try:
            domain = urllib3.util.url.parse_url(self.domain).host
        except Exception as e:
            print("Invalid domain, try again..")
            sys.exit(1)
        return domain
    
    def parse_wordlist(self):
        try:
        # print(wordlist)
            raw_data = open(self.wordlist,'r',errors='replace',encoding='utf-8').read().splitlines()
            # print(wordlists)
        except Exception as e:
            print(e)
            sys.exit(1)
        return raw_data
    
    def Scanner(self, domain, word_queue):
        while not word_queue.empty():
            subdomain = word_queue.get()
            url = f"http://{subdomain}.{domain}"
            try:
                res = requests.get(url)
            except Exception:
                pass
            else:
                print("[+] - %s - %d" %(url,res.status_code))
            word_queue.task_done()
    
    def run(self):
        subdomains = self.parse_wordlist()
        for subdomain in subdomains:
            self.word_queue.put(subdomain)
        for thread in range(self.threads):
            t = threading.Thread(target=self.Scanner,args=(self.domain,self.word_queue,))
            t.start()


if __name__ == "__main__":
    domain = "viblo.asia"
    wordlist = "/usr/share/wordlists/dirb/common.txt"
    threads = 100
    scanner = Sub(domain=domain,wordlist=wordlist,threads=threads)
    scanner.run()