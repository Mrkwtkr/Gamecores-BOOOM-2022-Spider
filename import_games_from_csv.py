"""CSV 数据导入 Notion

读取 BOOOM 2022 游戏爬虫储存在 CSV 的数据，将其上传至指定的 Notion 数据库，包括游戏标题、标签、图片、链接。

"""

import requests
import re
import json
import time
import pandas as pd

# 数据库 ID
game_db_id = "填入你的 Notion 数据库 ID"

# Token，在管理 Notion Integration 的网页可以获取到
# 别忘了先为 Integration 开启数据库的 edit 权限
token = "填入你的 token"

# HTML 请求头
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13',
}

# 读取 CSV 为 DataFrame
df = pd.read_csv("Gcores BOOOM 2022.csv", encoding="utf-8")
print(df)

# 任意新建一个带外部图片的页面，测试查看 Notion files 数据的格式
# url = f"https://api.notion.com/v1/databases/{game_db_id}/query"
# response = requests.request("POST", url, headers=headers)
# print(response.json()["results"][0]["properties"])

# 获取数据行数，逐条遍历
row_count = len(df.index)
for i in range(0, row_count):
    # 从 DF 提取数据
    data = df.iloc[i]
    title = data.title
    tags = data.tags
    tags = re.sub(r"[\'\"\s\[\]]", "", tags).split(",")
    tags_prop = []
    for tag in tags:
        tags_prop.append({"name": tag})
    game_url = data.game_url

    # 图片 URL 不正确会触发 400 错误，必须检查
    img_url = data.img_url
    try:
        img_url = re.search(r'.+\.(png|jpg|JPG|gif)', img_url).group()
    except AttributeError:
        print(img_url)
        
    # 为新建 Notion 准备数据结构
    # 务必提前在数据库中创建好对应名称、类别的属性，否则添加页面会报错
    game_prop_data = {
        "名称": {"title": [{"text": {"content": title}}]},
        "标签": {"multi_select": tags_prop},
        "链接": {"url": game_url},
        '封面图': {'files': [{'name': img_url, 'type': 'external', 'external': {'url': img_url}}]}
    }

    # 新建页面
    create_url = 'https://api.notion.com/v1/pages'
    # 创建 page 数据
    page_data = {
        "parent": { "database_id": game_db_id},
        "properties": game_prop_data
    }
    data = json.dumps(page_data)
    response = requests.request("POST", create_url, headers=headers, data=data)

    # 如果新建页面报错，打印出来便于排查
    status_code = response.status_code
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if status_code == 200:
        print(f"[{now}][INFO]成功新建页面")
    elif status_code == 400:
        print(f"[{now}][ERROR]创建页面时出错")
        print(f"[{now}][ERROR]prop_data: {game_prop_data}")
        print(f"[{now}][ERROR]response: {response.json()}")
