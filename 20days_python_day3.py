# 认识 HTML + 用 BeautifulSoup 提取数据
# 今日目标
# 看懂网页基本结构 HTML
# 安装并学会使用 BeautifulSoup
# 第一次真正从网页里提取标题、链接、文本
# 完成实战小练习
"""
必须记住 3 个名词
标签：<div> <a> <p> <span> 这种尖括号包裹的
属性：class="..." href="..." id="..."
内容：标签中间的文字
"""
# 实战：从豆瓣电影提取标题 + 评分
# 目标网址https://movie.douban.com/top250
import requests
from bs4 import BeautifulSoup
# 发送请求,带UA
url = "https://movie.douban.com/top250"
headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
}
res = requests.get(url , headers=headers)

# 处理编码
res.encoding = "utf-8"
# 创建 BeautifulSoup 对象
# beautifulsoup4：用来解析 HTML
# lxml：解析引擎，速度更快
soup = BeautifulSoup(res.text, "lxml")

# 查找单个标签：find(标签名, 属性)
#title_tag = soup.find("span", class_="title")
#print("单个电影标题:", title_tag.text.strip())
#strip()去掉字符串 开头和结尾 的空格、换行、空白符号。中间的空格不会动。
# 字符串.strip()        # 去掉首尾空白（空格、换行、制表符等）
# 字符串.lstrip()       # 只去掉左边（left）
# 字符串.rstrip()       # 只去掉右边（right）

# 查找多个标签 find_all(标签名 , 属性)
# all_titles = soup.find_all("span", class_="title")
# all_scores = soup.find_all("span", class_="rating_num")

# 5. 遍历输出
# 涉及知识点:
# zip() 的作用：把两个列表「一 一 对 应」打包在一起，方便循环同时取数据。
# 就像拉锁一样，把两边的元素一对一对扣起来。
# 超级简单记忆口诀:两个列表要配对，就用 zip ()！
# Python 列表 / 字符串切片格式：
# 变量 [ 起始位置 : 结束位置 : 步长 ]
# 第 1 个数字：从哪里开始（不写 = 从头开始）
# 第 2 个数字：到哪里结束（不写 = 直到最后）
# 第 3 个数字：步长（每隔几个取一个）

"""
print("\n=== 豆瓣 TOP250 前几条 ===")
for title, score in zip(all_titles[::2], all_scores):
    print(f"标题：{title.text.strip()} | 评分：{score.text}")
"""
# 由于豆瓣250页面有的电影有两个甚至更多名字,所以上面的方法行不通

# 定位到电影所在的大盒子,遍历所有的盒子信息,只取第一个名字
items = soup.find_all("div", class_="item")[:5]  #只取前五部电影
for item in items:
    title = item.find("span", class_="title").text.strip()
    score = item.find("span", class_="rating_num").text.strip()
    print(f"{title} | {score}")