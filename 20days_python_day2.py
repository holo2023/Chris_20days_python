"""
Day 2 核心知识点总结（必记）
状态码 200 = 成功
爬虫必须加 User-Agent 伪装浏览器
requests.get(url, headers=headers) 是标准写法
以后写爬虫，默认都带 headers，不要裸奔
"""
import requests

url = "https://movie.douban.com/top250"

# 不加headers直接请求,返回418代码
# 418 I'm a teapot（我是一个茶壶），是爬虫里非常经典的反爬拦截信号
# HTTP 418 是一个愚人节玩笑状态码，源自 1998 年的 RFC 2324（超文本咖啡壶控制协议）
# res1 = requests.get(url)
# print(res1.status_code)

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
print("状态码:" , response.status_code)
print("网页源码:" , "\n" , response.text[:100])