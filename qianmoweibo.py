# 阡陌微博视频
import requests

url = "https://f.video.weibocdn.com/o0/004kPuuQlx07TOh1yoNq01041200gw3g0E010.mp4?label=mp4_720p&template=1264x720.25.0&media_id=4737605938643074&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=4&ot=h&ps=3lckmu&uid=3ZoTIp&ab=,3601-g21,6377-g0,1192-g0,1191-g0,1046-g2,1258-g0&Expires=1710072092&ssig=OX7Rf3Sm7T&KID=unistore,video"

res = requests.get(
    url=url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "Referer": "https://weibo.com/"
    }

)
# print(res.text)
with open(f"video.mp4", mode='wb') as f:
    f.write(res.content)
