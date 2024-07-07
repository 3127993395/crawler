# 识别图像验证码
import ddddocr


with open("img/v1.jpg", mode="rb") as f:
    body = f.read()

ocr = ddddocr.DdddOcr(show_ad=False)
code = ocr.classification(body)
print(code)
