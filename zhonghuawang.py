# 中华网   https://passport.china.com/logon
import requests
from bs4 import BeautifulSoup


import requests
from bs4 import BeautifulSoup

res = requests.post(
    url="https://passport.china.com/logon",
    data={
        "userName": "13646285916",
        "password": "lzy13646285916"
    },
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Referer": "https://passport.china.com/logon",
        "Origin": "https://passport.china.com",
        "X-Requested-With": "XMLHttpRequest"
    }
)
# print(111111, res.text)
cookie_dict = res.cookies.get_dict()

res = requests.get(
    url="https://passport.china.com/main",
    cookies=cookie_dict
)

soup = BeautifulSoup(res.text, features="html.parser")
tag = soup.find(attrs={"id": "usernick"})
print(tag.text)
print(tag.attrs['title'])
