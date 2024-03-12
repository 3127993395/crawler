# 网易云音乐
import requests
from bs4 import BeautifulSoup

url = "https://music.163.com/discover/playlist/?cat=%E5%8D%8E%E8%AF%AD"

res = requests.get(
    url=url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "Referer": "https://music.163.com/"
    }

)

# print(res.text)
soup = BeautifulSoup(res.text, features="html.parser")
parent_tag = soup.find(name="ul", attrs={"id": "m-pl-container"})
for chind in parent_tag.find_all(recursive=False):
    title = chind.find(name="a", attrs={"class": "tit f-thide s-fc0"}).text
    print(title)
    image_url = chind.find(name="img").attrs['src']
    print(image_url)

    # 下载每个封面
    img_res = requests.get(url=image_url)
    file_name = title.split()[0]
    with open(f"{file_name}.jpg", mode='wb') as f:
        f.write(img_res.content)
