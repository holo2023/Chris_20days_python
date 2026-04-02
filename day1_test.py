"""
练习 1
把网址换成：https://www.qq.com爬取腾讯首页，观察输出。
练习 2
尝试打印：
python
运行
print(response.encoding)   # 网页编码
print(response.url)        # 实际访问的地址
练习 3（简单思考）
为什么爬出来的内容是一堆乱码一样的东西？
"""

# 导入requests库
import requests

# 目标网址
url = "https://www.qq.com"

# 发送请求
response = requests.get(url)

# 打印网页编码
response.encoding = "utf-8"
#print("网页编码:" , response.encoding)

# 打印实际访问的网址
#print("实际访问的网址:" , response.url)

print(response.text[:500]) #[:500]指的是取前500个字符