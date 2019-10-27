"""
编写程序访问百度首页，并获得响应
"""
import urllib.request
# urlopen():向URL发送请求，返回响应对象
response = urllib.request.urlopen("http://www.baidu.com/")
# 获取响应内容
html = response.read().decode('utf8')
# 打印响应内容
print(html)

