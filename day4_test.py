# 今日课后练习
# 把爬取页数改成 10 页（爬完整 250 部）
# 同时爬取引言（class="inq"），一起保存到文件
# 尝试只保存评分 9.5 分以上的电影
# https://movie.douban.com/top250

import requests
from bs4 import BeautifulSoup

headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
}

with open("douban_top250n.txt", "w", encoding="utf-8") as f:

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
            # 正确写法（先判断有没有，再取值）
            # 层级问题：引言在 <p class="quote"> 里面的 <span> 标签里，直接找 <span class="quote"> 找不到
            # 爬取网页元素时，必须严格匹配标签的嵌套层级和属性：
            # 先看外层容器（如 <p class="quote">）；
            # 再在容器内找目标子标签（如里面的 <span>）；
            # 永远加判断，避免找不到标签时报错。
            quote_tag = item.find("p", class_="quote")
            if quote_tag:
                quote = quote_tag.find("span").text.strip()
            else:
                quote = "无引言"

            # 打印 + 写入文件
            line = f"电影：{title}  评分：{score}  引言:{quote}\n"
            print(line.strip())
            f.write(line)