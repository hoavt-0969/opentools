# params_fuzz = [
#     'name','query','redirect', 'redir', 'url', 'link', 'goto', 'debug', '_debug', 'test', 'get', 'index', 'src', 'source', 'file',
#     'frame', 'config', 'new', 'old', 'var', 'rurl', 'return_to', '_return', 'returl', 'last', 'text', 'load', 'email',
#     'mail', 'user', 'username', 'password', 'pass', 'passwd', 'first_name', 'last_name', 'back', 'href', 'ref', 'data', 'input',
#     'out', 'net', 'host', 'address', 'code', 'auth', 'userid', 'auth_token', 'token', 'error', 'keyword', 'key', 'q', 'aid',
#     'bid', 'cid', 'did', 'eid', 'fid', 'gid', 'hid','id', 'iid', 'jid', 'kid', 'lid', 'mid', 'nid', 'oid', 'pid', 'qid', 'rid', 'sid',
#     'tid', 'uid', 'vid', 'wid', 'xid', 'yid', 'zid', 'cal', 'country', 'x', 'y', 'topic', 'title', 'head', 'higher', 'lower', 'width',
#     'height', 'add', 'result', 'log', 'demo', 'example', 'message', 'page', 's','search']

# import requests
# from http.cookies import SimpleCookie
# url = "https://abunabi-asado.tk/vulnerabilities/xss_r/"
# rawdata = "PHPSESSID=crbhf2iacuphob4kfn92g87gn2; security=low"


# cookie = SimpleCookie()
# cookie.load(rawdata)

# # Even though SimpleCookie is dictionary-like, it internally uses a Morsel object
# # which is incompatible with requests. Manually construct a dictionary instead.
# cookies = {}
# for key, data in cookie.items():
#     cookies[key] = data.value
# print(cookies)
# # res = requests.get(url,cookies=cookies)
# # print(res.content.decode())

import argparse


# since we are now passing in the greeting
# the logic has been consolidated to a single greet function
def greet(args):
    output = '{0}, {1}!'.format(args.greeting, args.name)
    if args.caps:
        output = output.upper()
    print(output)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='command',dest='command')

hello_parser = subparsers.add_parser('hello')
hello_parser.add_argument('name')
# add greeting option w/ default
hello_parser.add_argument('--greeting', default='Hello')
# add a flag (default=False)
hello_parser.add_argument('--caps', action='store_true')
hello_parser.set_defaults(func=greet)

goodbye_parser = subparsers.add_parser('goodbye')
goodbye_parser.add_argument('name')
goodbye_parser.add_argument('--greeting', default='Goodbye')
goodbye_parser.add_argument('--caps', action='store_true')
goodbye_parser.set_defaults(func=greet)

if __name__ == '__main__':
    args = parser.parse_args()
    print(vars(args))
    # print(vars(args))
    args.func(args)