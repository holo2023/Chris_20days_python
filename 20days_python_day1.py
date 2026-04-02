#  Day1 核心理论总结（必记）
#  1.requests.get(url) → 访问网页
#  2.response.status_code → 看是否成功（200 = 成功）
#  3.response.text → 网页源代码
#  4.爬虫最基础结构就是：请求 → 获取内容

# 导入requests库
import requests
# 指定目标网址
url = "https://www.baidu.com"

# 发送请求
response = requests.get(url)

# 打印状态码(200代表成功)
print("状态码" , response.status_code)

# 打印网页源代码
print("网页内容:" "\n" , response.text)

