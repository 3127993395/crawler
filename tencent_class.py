# 腾讯课堂
import requests

res = requests.get(
    url='https://ke.qq.com/cgi-proxy/home/web_home_course?category1st=1000&model_id=3&must_not_courses=%5B%5D&page_num=3&page_size=19&platform=3&bkn=&r=0.7846',
    headers={
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        "Referer": 'https://ke.qq.com/',
    },
)

print(res.text)
