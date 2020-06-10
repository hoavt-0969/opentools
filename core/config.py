import argparse
from core import parsedata
def parse_cookie(rawdata):
    if rawdata == None:
        return rawdata
    from http.cookies import SimpleCookie
    cookie = SimpleCookie()
    cookie.load(rawdata)
    cookies = {}
    for key, data in cookie.items():
        cookies[key] = data.value
    return cookies

def options():
    parser = argparse.ArgumentParser(prog="scan")
    subparsers = parser.add_subparsers(dest='command')

    dirb_parser = subparsers.add_parser("dirb")
    xss_parser = subparsers.add_parser("xss")
    dns_parser = subparsers.add_parser("dns")

    dirb_parser.add_argument('-u','--url',required=True,type=str,default=None)
    dirb_parser.add_argument('-w','--wordlist',type=str,required=True,default="/home/sun/opentools/subdomains.txt")
    dirb_parser.add_argument("-e","--extensions",type=str,required=True,default=".php,.html,.txt")
    dirb_parser.add_argument("-t", "--threads",default=10,type=int,help="Set number threads", required=False)

    xss_parser.add_argument('-u','--url',required=True,type=str)
    xss_parser.add_argument('--cookies', required=False,type=str)
    xss_parser.add_argument('--proxy',required=False,type=str,default="http://localhost:8080")

    # parser.add_argument('--cookies',type=str, required=False, help="Set cookies")
    return parser.parse_args()


args = options()

# print(vars(args))
# print(args.command)
if args.command == "dirb":
    if args.url[-1] == "/":
        url = args.url[:-1]
    else:
        url = args.url
    # print(url[-1])
    # print(url)
    number_threads = args.threads
    cookies = parsedata.parse_cookie(args.cookies)
    wordlist = args.wordlist
    extensions = args.extensions.split(",")
    from core import dirb
    dirb.main()
    # print(vars(url))
    # print(vars(cookies))
    # print(vars(wordlist))
elif args.command == "xss":
    url = args.url
    params_fuzz = [
    'name','query','redirect', 'redir', 'url', 'link', 'goto', 'debug', '_debug', 'test', 'get', 'index', 'src', 'source', 'file',
    'frame', 'config', 'new', 'old', 'var', 'rurl', 'return_to', '_return', 'returl', 'last', 'text', 'load', 'email',
    'mail', 'user', 'username', 'password', 'pass', 'passwd', 'first_name', 'last_name', 'back', 'href', 'ref', 'data', 'input',
    'out', 'net', 'host', 'address', 'code', 'auth', 'userid', 'auth_token', 'token', 'error', 'keyword', 'key', 'q', 'aid',
    'bid', 'cid', 'did', 'eid', 'fid', 'gid', 'hid', 'iid', 'jid', 'kid', 'lid', 'mid', 'nid', 'oid', 'pid', 'qid', 'rid', 'sid',
    'tid', 'uid', 'vid', 'wid', 'xid', 'yid', 'zid', 'cal', 'country', 'x', 'y', 'topic', 'title', 'head', 'higher', 'lower', 'width',
    'height', 'add', 'result', 'log', 'demo', 'example', 'message']
    payloads = "<script>alert(\"tested\");</script>"
    number_threads = 100
    cookies = parsedata.parse_cookie(args.cookies)
    proxies = None
    proxies = {
        'http': args.proxy,
        'https' : args.proxy,
    }
    print(proxies)
    from core import scanxss
    scanxss.main()
elif args.command == "dns":
    pass

# url = args.url
#cookies = parse_cookie(args.cookies)

# print(vars(args))
# print(extensions)



# cookies = {"PHPSESSID":"9ej49jdjq07nur1tuj5akfh67r", "security":"low"}




# wordlist_file = "/home/sun/opentools/subdomains.txt"

# extensions = [".php",".html",".txt"]