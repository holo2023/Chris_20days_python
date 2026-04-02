# 主题：多页爬取 + 数据保存到本地文件
# 今日目标
# 看懂豆瓣分页规律
# 用 for 循环自动爬取多页数据
# 把爬到的数据保存为 .txt / .csv 文件
# 学会通用的翻页爬虫写法
"""
多页爬虫核心思路
构造一个循环：for page in range(10)
每次生成对应页码的 URL
依次请求每一页
统一解析、保存数据
"""

# 第一页https://movie.douban.com/top250
# 第二页https://movie.douban.com/top250?start=25&filter=
# 第三页https://movie.douban.com/top250?start=50&filter=

import requests
from bs4 import BeautifulSoup

headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
}

# 打开文件，写入模式，utf-8 编码
with open("douban_top250.txt", "w", encoding="utf-8") as f:

    for page in range(3) :
        start = page * 25
        url = f"https://movie.douban.com/top250?start={start}&filter="
        print(f"===== 正在爬第 {page+1} 页，start={start} =====")
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "lxml")
        items = soup.find_all("div", class_="item")
        for item in items:
            title = item.find("span", class_="title").text.strip()
            score = item.find("span", class_="rating_num").text.strip()

            # 打印 + 写入文件
            line = f"电影：{title}  评分：{score}\n"
            print(line.strip())
            f.write(line)


# Day4 核心知识点总结
# 分页关键：找 URL 里的数字规律
# 多页爬取：for 循环 + 拼接 URL
# 保存文件：
# .txt：简单直接
# .csv：适合表格、Excel
# 编码统一用 encoding="utf-8"，避免中文乱码
