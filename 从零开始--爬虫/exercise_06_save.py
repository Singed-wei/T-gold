"""
在百度中输入要搜索的内容，把响应内容保存到本地文件
输入赵丽颖，保存到本地文件--赵丽颖1.html
"""
from urllib import request, parse


# 拼接url地址
def get_url(word):
    url = 'http://www.baidu.com/s?{}'
    params = parse.urlencode({'wd': word})
    url = url.format(params)
    return url


# 发请求，保存本地文件
def request_url(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0'}
    # 请求对象  +  响应对象  +  提取内容
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存数据
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


# 主程序入口
if __name__ == '__main__':
    word = input("请输入搜索内容：")
    url = get_url(word)
    filename = word + '.html'
    request_url(url, filename)
    # 看看是不是多了赵丽颖.html!!!!!
