# 软文街
import requests
import ddddocr

url = "https://api.ruanwen.la/api/auth/captcha/generate"
res = requests.post(
    url=url
)
res_dict = res.json()
# print(res_dict)
# print(res_dict['data']['captcha_token'])
captcha_token = res_dict['data']['captcha_token']
captcha_src = res_dict['data']['src']
res = requests.get(url=captcha_src)

with open("ruanwen.png", mode="wb") as f:
    f.write(res.content)

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(res.content)

# 登录认证
response = requests.post(
    url="https://api.ruanwen.la/api/auth/authenticate",
    json={
        "captcha": code,
        "captcha_token": captcha_token,
        "device": "pc",
        "identity": "advertiser",
        "mobile": "15850791986",
        "password": "1231213",
    }
)
print(response.json())
