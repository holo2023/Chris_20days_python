# Day6 学习目标
# 理解 字典嵌套取值（JSON 里一层又一层怎么拿）
# 学会 安全取值，不报错
# 接口爬虫 翻页加载更多
# 把数据保存成 JSON 文件
# 先回顾一句最重要的（今天全靠它）>>> 字典.get(键, 找不到时用的默认值)

import requests
import json

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36" ,
    "Referer":"https://m.douban.com/explore"
}
for page in range(3) :
    start = page * 20
    url = f"https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start={start}&limit=20"
    response = requests.get(url , headers=headers)
    data = response.json()
    movies = data.get("items" , [])
    print(f"=====开始打印第{page + 1}页=====")
    for movie in movies :
        title = movie["title"]
        score = movie["rating"]["value"]
        if score :
            score = score  #这么写对吗?
        else :
            score= "暂无评分"
        line = f"电影名:{title} 评分:{score}\n"
        print(line.strip())
