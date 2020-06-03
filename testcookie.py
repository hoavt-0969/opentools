import requests

cookies = dict(login="test/test")

r = requests.get("http://testphp.vulnweb.com/userinfo.php",cookies=cookies)
print(r.content.decode().find("(test)"))