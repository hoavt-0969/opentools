import argparse

def parse_cookie(rawdata):
    from http.cookies import SimpleCookie
    cookie = SimpleCookie()
    cookie.load(rawdata)
    cookies = {}
    for key, data in cookie.items():
        cookies[key] = data.value
    return cookies
def banner():
    print('''
 ____               ____ ____  ____  
/ ___| _   _ _ __  / ___/ ___||  _ \ 
\___ \| | | | '_ \| |   \___ \| |_) |
 ___) | |_| | | | | |___ ___) |  _ < 
|____/ \__,_|_| |_|\____|____/|_| \_\ 

''')

def options():
    parser = argparse.ArgumentParser(prog="scan")
    parser.add_argument("-u","--url",required=True)
    parser.add_argument("-t", "--threads",default=10,type=int,help="Set number threads")
    parser.add_argument('--cookies',type=str, required=False, help="Set cookies")
    parser.add_argument('-w','--wordlist',type=str,required=False,default="/home/sun/opentools/subdomains.txt")
    parser.add_argument("-e","--extensions",type=str,required=False,default=".php,.html,.txt")
    return parser.parse_args()

args = options()
url = args.url
number_threads = args.threads
cookies = parse_cookie(args.cookies)
extensions = args.extensions.split(",")
print(vars(args))
# print(extensions)
params_fuzz = [
    'name','query','redirect', 'redir', 'url', 'link', 'goto', 'debug', '_debug', 'test', 'get', 'index', 'src', 'source', 'file',
    'frame', 'config', 'new', 'old', 'var', 'rurl', 'return_to', '_return', 'returl', 'last', 'text', 'load', 'email',
    'mail', 'user', 'username', 'password', 'pass', 'passwd', 'first_name', 'last_name', 'back', 'href', 'ref', 'data', 'input',
    'out', 'net', 'host', 'address', 'code', 'auth', 'userid', 'auth_token', 'token', 'error', 'keyword', 'key', 'q', 'aid',
    'bid', 'cid', 'did', 'eid', 'fid', 'gid', 'hid', 'iid', 'jid', 'kid', 'lid', 'mid', 'nid', 'oid', 'pid', 'qid', 'rid', 'sid',
    'tid', 'uid', 'vid', 'wid', 'xid', 'yid', 'zid', 'cal', 'country', 'x', 'y', 'topic', 'title', 'head', 'higher', 'lower', 'width',
    'height', 'add', 'result', 'log', 'demo', 'example', 'message']


# cookies = {"PHPSESSID":"9ej49jdjq07nur1tuj5akfh67r", "security":"low"}

payloads = "<script>alert(\"tested\");</script>"



# wordlist_file = "/home/sun/opentools/subdomains.txt"

# extensions = [".php",".html",".txt"]