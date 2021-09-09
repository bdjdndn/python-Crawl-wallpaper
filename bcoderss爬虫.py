import requests
import re
import pprint

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"

}
title = "美女"

# 构建请求地址
for pag in range(2, 50):
    url = f"https://m.bcoderss.com/tag/{title}/page/{pag}//"
    print(f"----------------------正在爬取第{pag}页----------------------------------")
    response = requests.get(url=url, headers=headers)
    url_data = response.text
    # print(url_data)
    #
    # 获取图片url地址并对其地址发送get请求
    img_url = re.findall(
        '<img width=".*?" height=".*?" src="(.*?)" class="attachment-thumbnail size-thumbnail wp-post-image" alt=".*?" title=".*?" /',
        url_data, re.S)
    # print(img_url)

    # <img width="260" height="534" src=".*?" class="attachment-thumbnail size-thumbnail wp-post-image" alt="(.*?)" title=".*?" />

    # 获取图片名字
    img_name = re.findall(
        '<img width="260" height="534" src=".*?" class="attachment-thumbnail size-thumbnail wp-post-image" alt="(.*?)" title=".*?" />',
        url_data, re.S)
    # print(img_name)

    # 保存数据
    for url_data, file_name in zip(img_url, img_name):
        # 遍历出名字和请求地址
        # print(url_data + file_name)
        img_data = requests.get(url=url_data, headers=headers)
        img_data_img = img_data.content
        with open('img\\'+file_name + ".jpg", mode='wb') as f:
            f.write(img_data_img)
            print('保存完成: ', file_name)
