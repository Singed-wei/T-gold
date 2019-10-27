"""
向测试网站：http://httpbin.org/get发请求，查看自己请求头
网站在检查请求时，请求头一定是最先被检查的，先来看看我们使用程序访问网站的时候请求头是怎么样的
"""
import urllib.request
response = urllib.request.urlopen("http://httpbin.org/get")
html = response.read().decode()
print(html)
# "headers": {
#     "Accept-Encoding": "identity",
#     "Host": "httpbin.org",
#     "User-Agent": "Python-urllib/3.6"
#   },
# 可以看到我们的请求头居然有明显的python-urllib/3.6!显然在正式爬虫中是不可行的。所以我们需要重构User-Agent.

