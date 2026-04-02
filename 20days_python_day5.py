# #主题：抓包分析 | 直接请求接口数据（速度提升 10 倍）
# 今日目标
# 掌握 浏览器开发者工具 (F12) 的使用
# 学会 寻找真实数据接口 (API)
# 理解 JSON 数据格式（比 HTML 好处理 100 倍）
# 完成 豆瓣电影 TOP250 接口版 爬虫（更稳、更快）

import requests
import json  # 必须导入 json 库

# 1. 设定请求头（模拟浏览器）
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36" ,
    "Referer":"https://m.douban.com/explore"
}

# 2. 获取【接口】URL
# 真实场景下，你需要通过抓包获得真实的接口地址

url = "https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start=0&limit=20"

# 3. 发送请求 (获取 JSON 数据)
# 这里用 .get() 方法，和之前一样
response = requests.get(url, headers=headers)

# 4. 解析 JSON 数据 (核心步骤！)
# response.text 是字符串，我们转成 Python 字典
data = response.json()

# 5. 提取数据 (JSON 数据结构通常是：列表里套字典)
# 抓包到的json数据
# items[{rating: {count: 72149, max: 10, star_count: 3, value: 6.1}, title: "呼啸山庄",…},…]
#  JSON 里 key 叫 "items" 存电影列表
movies = data.get("items", [])

for movie in movies:
    # 注意：JSON 里用 ["键名"] 取值，或者 .get() 方法
    title = movie["title"]
    score = movie["rating"]["value"]  # 嵌套数据，一层一层找

    print(f"电影：{title} | 评分：{score}")
