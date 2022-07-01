# Gamecores-BOOOM-2022-Spider
从 [机核 BOOOM 官方页面](https://site.gcores.com/booom2022/games/) 收集游戏数据，并导入指定 Notion 数据库的几个脚本。<br>
Python scripts to collect game data from [Gamecores official list](https://site.gcores.com/booom2022/games/), and import them to a Notion database.

# 效果展示
可参考我分享的这个 [游戏库](https://mrkwtkr.notion.site/cd98467e04044aad8ee93771bf9e8c28?v=25f3e029ff4d4329a2fc4d3841020e84)

# 如何使用
## 从 BOOOM 页面爬取数据
1. 选择一个目录存放这些文件
2. 访问 Chromedriver 的 [官网](https://chromedriver.chromium.org/downloads), 基于你的 Chrome 版本下载对应的 chromedriver
3. 将 chromedriver.exe 放在和爬虫脚本 `spider.py` 相同的目录下
4. 运行爬虫脚本, 等待爬取数据
5. 完成

## 将数据导入 Notion
1. 在文件 `import_games_from_csv.py` 中，将 `game_db_id` 填写为你要导入的数据库 ID，`token` 填写你机器人的 token 
2. 参考 `game_prop_data` 中的数据格式，在你的数据库中创建对应名称、类型的属性，以便正常新建页面
3. 运行导入数据的脚本 `import_games_from_csv.py`

# Outcome
As shown in this [Notion database](https://mrkwtkr.notion.site/cd98467e04044aad8ee93771bf9e8c28?v=25f3e029ff4d4329a2fc4d3841020e84)

# How to
## Start collecting games' data from BOOOM
1. Select a directory and put the files
2. Access Chromedriver's [official website](https://chromedriver.chromium.org/downloads), Download chromedriver based on your Chrome version
3. Put the chromedriver.exe in the same directory of the spider file `spider.py`
4. Execute the spider, wait for collecting data
5. Done

## Import data to a Notion database
1. Use the db_id and toke of your integration in `import_games_from_csv.py`
2. Create properties in Notion database as shown by `game_prop_data` in `import_games_from_csv.py`
3. Execute `import_games_from_csv.py`
