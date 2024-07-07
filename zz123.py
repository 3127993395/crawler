# 反调试(禁用域名)
# www.zz123.com
import requests

url = "https://zz123.com/ajax/"
res = requests.post(
    url=url,
    data={
        "act": "hotsearch",
    }
)
res_dict = res.json()
print(res_dict)

# data_list = res_dict['data']
# for item in data_list:
#     print(item)