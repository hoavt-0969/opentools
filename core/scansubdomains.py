import requests
import urllib3
import sys
import threading

from queue import Queue

d = Queue()

def parse_url(url):
    try:
        host = urllib3.util.url.parse_url(url).host
    except Exception as e:
        print("Invalid domain, try again..")
        sys.exit(1)
    return host

def parse_wordlist(wordlist):
    try:
        wordlists = open(wordlist).read().splitlines()
    except Exception as e:
        print(e)
        sys.exit(1)
    return wordlists
def banner():
    print('''
 ____               ____ ____  ____  
/ ___| _   _ _ __  / ___/ ___||  _ \ 
\___ \| | | | '_ \| |   \___ \| |_) |
 ___) | |_| | | | | |___ ___) |  _ < 
|____/ \__,_|_| |_|\____|____/|_| \_\ 
=====================================
''')

def scan_subdomain(target):
    global d
    while True:
        subdomain = d.get()
        url = f"http://{subdomain}.{target}"
        try:
            res = requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            if res.status_code == 200:
                print("[+] ", url)
        d.task_done()

def mutil_scan_subdomains(target,number_threads,subdomains):
    for subdomain in subdomains:
        d.put(subdomain)
    for thread in range(number_threads):
        t = threading.Thread(target=scan_subdomain, args=(target,))
        t.daemon = True
        t.start()
def main():
    target = input("Target: ")
    wordlist = input("Wordlist: ")
    number_threads = int(input("Number threads: "))
    print("=====================")
    mutil_scan_subdomains(target=target, number_threads=number_threads,subdomains=parse_wordlist(wordlist))
if __name__ == "__main__":
    banner()
    print("====================")
    main()
    d.join()