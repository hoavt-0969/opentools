params_fuzz = [
    'name','query','redirect', 'redir', 'url', 'link', 'goto', 'debug', '_debug', 'test', 'get', 'index', 'src', 'source', 'file',
    'frame', 'config', 'new', 'old', 'var', 'rurl', 'return_to', '_return', 'returl', 'last', 'text', 'load', 'email',
    'mail', 'user', 'username', 'password', 'pass', 'passwd', 'first_name', 'last_name', 'back', 'href', 'ref', 'data', 'input',
    'out', 'net', 'host', 'address', 'code', 'auth', 'userid', 'auth_token', 'token', 'error', 'keyword', 'key', 'q', 'aid',
    'bid', 'cid', 'did', 'eid', 'fid', 'gid', 'hid','id', 'iid', 'jid', 'kid', 'lid', 'mid', 'nid', 'oid', 'pid', 'qid', 'rid', 'sid',
    'tid', 'uid', 'vid', 'wid', 'xid', 'yid', 'zid', 'cal', 'country', 'x', 'y', 'topic', 'title', 'head', 'higher', 'lower', 'width',
    'height', 'add', 'result', 'log', 'demo', 'example', 'message', 'page', 's','search']

import requests
from http.cookies import SimpleCookie
url = "https://abunabi-asado.tk/vulnerabilities/xss_r/"
rawdata = "PHPSESSID=crbhf2iacuphob4kfn92g87gn2; security=low"


cookie = SimpleCookie()
cookie.load(rawdata)

# Even though SimpleCookie is dictionary-like, it internally uses a Morsel object
# which is incompatible with requests. Manually construct a dictionary instead.
cookies = {}
for key, data in cookie.items():
    cookies[key] = data.value
print(cookies)
# res = requests.get(url,cookies=cookies)
# print(res.content.decode())