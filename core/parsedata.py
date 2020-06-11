from http.cookies import SimpleCookie
import urllib3
import sys

def parse_cookie(rawdata):
    if rawdata == None:
        return rawdata
    cookie = SimpleCookie()
    cookie.load(rawdata)
    cookies = {}
    for key, data in cookie.items():
        cookies[key] = data.value
    return cookies

# def parse_url(url):
#     try:
#         host = urllib3.util.url.parse_url(url).host
#     except Exception as e:
#         print("Invalid domain, try again..")
#         sys.exit(1)
#     return host
# def parse_wordlist(wordlist):
#     try:
#         wordlists = open(wordlist).read().splitlines()
#     except Exception as e:
#         print(e)
#         sys.exit(1)
#     return wordlists