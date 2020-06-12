# # # params_fuzz = [
# # #     'name','query','redirect', 'redir', 'url', 'link', 'goto', 'debug', '_debug', 'test', 'get', 'index', 'src', 'source', 'file',
# # #     'frame', 'config', 'new', 'old', 'var', 'rurl', 'return_to', '_return', 'returl', 'last', 'text', 'load', 'email',
# # #     'mail', 'user', 'username', 'password', 'pass', 'passwd', 'first_name', 'last_name', 'back', 'href', 'ref', 'data', 'input',
# # #     'out', 'net', 'host', 'address', 'code', 'auth', 'userid', 'auth_token', 'token', 'error', 'keyword', 'key', 'q', 'aid',
# # #     'bid', 'cid', 'did', 'eid', 'fid', 'gid', 'hid','id', 'iid', 'jid', 'kid', 'lid', 'mid', 'nid', 'oid', 'pid', 'qid', 'rid', 'sid',
# # #     'tid', 'uid', 'vid', 'wid', 'xid', 'yid', 'zid', 'cal', 'country', 'x', 'y', 'topic', 'title', 'head', 'higher', 'lower', 'width',
# # #     'height', 'add', 'result', 'log', 'demo', 'example', 'message', 'page', 's','search']

# # # import requests
# # # from http.cookies import SimpleCookie
# # # url = "https://abunabi-asado.tk/vulnerabilities/xss_r/"
# # # rawdata = "PHPSESSID=crbhf2iacuphob4kfn92g87gn2; security=low"


# # # cookie = SimpleCookie()
# # # cookie.load(rawdata)

# # # # Even though SimpleCookie is dictionary-like, it internally uses a Morsel object
# # # # which is incompatible with requests. Manually construct a dictionary instead.
# # # cookies = {}
# # # for key, data in cookie.items():
# # #     cookies[key] = data.value
# # # print(cookies)
# # # # res = requests.get(url,cookies=cookies)
# # # # print(res.content.decode())

# # import argparse


# # # since we are now passing in the greeting
# # # the logic has been consolidated to a single greet function
# # def greet(args):
# #     output = '{0}, {1}!'.format(args.greeting, args.name)
# #     if args.caps:
# #         output = output.upper()
# #     print(output)

# # parser = argparse.ArgumentParser()
# # subparsers = parser.add_subparsers(help='command',dest='command')

# # hello_parser = subparsers.add_parser('hello')
# # hello_parser.add_argument('name')
# # # add greeting option w/ default
# # hello_parser.add_argument('--greeting', default='Hello')
# # # add a flag (default=False)
# # hello_parser.add_argument('--caps', action='store_true')
# # hello_parser.set_defaults(func=greet)

# # goodbye_parser = subparsers.add_parser('goodbye')
# # goodbye_parser.add_argument('name')
# # goodbye_parser.add_argument('--greeting', default='Goodbye')
# # goodbye_parser.add_argument('--caps', action='store_true')
# # goodbye_parser.set_defaults(func=greet)

# # if __name__ == '__main__':
# #     args = parser.parse_args()
# #     print(vars(args))
# #     # print(vars(args))
# #     args.func(args)

# # import sys
# # def parse_wordlist(wordlist):
# #     try:
# #         wordlists = open(wordlist).read().splitlines()
# #     except Exception as e:
# #         print(e)
# #         sys.exit(1)
# #     return wordlists

# # from queue import Queue
# # wordlist_path = '/usr/share/wordlists/dirb/big.txt'

# # # wordlist = parse_wordlist(wordlist_path)

# # # print(wordlist)
# # resume = None
# # raw_words = []

# # def build_wordlist(wordlist_file):

# #     f = open(wordlist_file,"r")
# #     raw_word = f.readline()
# #     while raw_word != '':
# #         try:
# #             raw_word = f.readline()
# #             raw_words.append(raw_word)
# #         except:
# #             pass
# #     f.close()
# #     found_resume = False
# #     words = Queue()
# #     for word in raw_words:
# #         word = word.rstrip()
# #         if resume is not None:
# #             if found_resume:
# #                 words.put(word)
# #             else:
# #                 if word == resume:
# #                     found_resume = True
# #         else:
# #             words.put(word)
# #     return words


# # data = build_wordlist(wordlist_path)
# # while not data.empty():
# #     print(data.get())
# # print(data)
#     # found_resume = False
#     # words = Queue()
#     # for word in raw_words:
#     #     word = word.rstrip()
#     #     if resume is not None:
#     #         if found_resume:
#     #             words.put(word)
#     #         else:
#     #             if word == resume:
#     #                 found_resume = True
#     #     else:
#     #         words.put(word)
#     # return words
# import requests
# import threading
# from queue import Queue
# import sys
# import urllib
# class Dirb(object):
#     def __init__(self, url, extensions, wordlist, cookies=None, headers=None,number_threads=50,proxies=None):
#         self.url = url
#         self.extensions = extensions
#         self.wordlist = wordlist
#         self.cookies = cookies
#         self.headers = headers
#         self.number_threads = number_threads
#         self.proxies = proxies
#         self.resume = None

#     def load_wordlist(self):
#         try:
#             raw_data = open(self.wordlist,'r').read().splitlines()
#         except Exception as e:
#             print(e)
#             sys.exit(1)
#         return raw_data
    
#     def build_wordlist(self):
#         found_resume = False
#         raw_words = self.load_wordlist()
#         words = Queue()
#         for word in raw_words:
#             word = word.rstrip()
#             if self.resume is not None:
#                 if found_resume:
#                     words.put(word)
#                 else:
#                     if word == self.resume:
#                         found_resume = True
#             else:
#                 words.put(word)
        
#         return words

#     def Scanner(self):
#         # print('hello')
#         words = self.build_wordlist()
#         while not words.empty():
#             attempt = words.get()
#             attempt_list = []
#             if "." not in attempt:
#                 attempt_list.append("/%s/" %attempt)
#             else:
#                 attempt_list.append("/%s/" %attempt)
#             if self.extensions:
#                 for extension in self.extensions:
#                     attempt_list.append("/%s%s"%(attempt,extension))
#             for brute in attempt_list:
#                 url = "%s%s" %(self.url,brute)
#                 print(brute)
#                 # print(url)
#                 res = requests.get(url,cookies=self.cookies, allow_redirects=False, proxies=self.proxies,)
#                 if res.status_code !=404:
#                     print("+ [%d] - %s"%(res.status_code,url))
#         words.task_done()

#     def run(self):
#         for thread in range(self.number_threads):
#             t = threading.Thread(target=self.Scanner,args=())
#             t.daemon = True
#             t.start()



# if __name__ == "__main__":
#     url = "http://testphp.vulnweb.com"
#     threads = 100
#     extensions = ['.php','.html','.txt']
#     wordlist = "/home/sun/opentools/test1.txt"
#     scanner = Dirb(url=url,extensions=extensions,wordlist=wordlist,number_threads=threads)
#     scanner.run()


def load_wordlist(path):
    result = ''
    with open(path,'r', errors="replace",encoding='utf-8') as fd:
        return fd.read().splitlines()


path = '/usr/share/wordlists/dirb/big.txt'


raw = load_wordlist(path)
# print(len(raws))
# print(raw.splitlines())
print(raw)
# for raw in raws:
#     print(raw)