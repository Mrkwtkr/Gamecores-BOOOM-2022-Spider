"""机核网 BOOOM 2022 页面爬虫

用 Selenium 访问机核网 2022 页面，通过模拟滚动操作、提取页面信息，收集此届参赛的作品数据。

"""

from selenium import webdriver
import time
import re

# 指定 chromedriver 路径，打开网页信息
url = "https://site.gcores.com/booom2022/games/"
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

# 模拟向下滚动页面，直至页面高度不再刷新
height = 0
while True:
    new_height = driver.execute_script("return document.documentElement.scrollHeight;")
    # 每执行一次滚动条拖到最后，就进行一次参数校验，并且刷新页面高度
    if new_height > height:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        height = new_height
        time.sleep(1)
    else:
        # 当页面高度不再增加的时候，我们就认为已经是页面最底部，结束条件判断
        print("滚动条已经处于页面最下方!")
        driver.execute_script('window.scrollTo(0, 0)')  # 把滚动条拖到页面顶部
        break

# 提取游戏数据
games = []
# 类似 Scrapy，先提取元素遍历，再提取其中包含的各项数据
for game in driver.find_elements_by_xpath("//a[@class='gamesList-module--game--dlIE2']"):
    # 文本使用 .text
    title = game.find_element_by_xpath("./div/h3").text
    tags = []
    for tag in game.find_elements_by_xpath("./div/p/span"):
        tags.append(tag.text)
    # 属性用 get_attribute，不能用 xpath 的 @xxx
    game_url = game.get_attribute("href")
    img_url = game.find_element_by_xpath("./img").get_attribute("src")
    data = {
        "title": title,
        "tags": tags,
        "game_url": game_url,
        "img_url": img_url,
    }
    games.append(data)
    print(data)

# 数据写入 CSV
import pandas as pd
df = pd.DataFrame(games)
df.to_csv("Gcores BOOOM 2022.csv", index=False, sep=",")
