# 北大未名 https://bbs.pku.edu.cn/v2/home.php
import time
import requests
import hashlib

res = requests.get(url="https://bbs.pku.edu.cn/v2/home.php", )
cookie_dict = res.cookies.get_dict()
# print(cookie_dict)  # {'skey': 'ed252f6a317f098e', 'uid': '15265'}

user = "zhangkai"
pwd = "123123"
ctime = int(time.time())
data_string = f"{pwd}{user}{ctime}{pwd}"
obj = hashlib.md5()
obj.update(data_string.encode('utf-8'))
md5_string = obj.hexdigest()

res = requests.post(
    url="https://bbs.pku.edu.cn/v2/ajax/login.php",
    data={
        "username": user,
        "password": pwd,
        "keepalive": "0",
        "time": ctime,
        "t": md5_string
    },
    cookies=cookie_dict
)

print(res.text)
