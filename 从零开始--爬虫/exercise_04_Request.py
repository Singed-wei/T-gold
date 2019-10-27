"""
urllib.request.Request方法用来创建请求对象，包装请求，重构User-Agent.
"""
import urllib.request
# 1、构造请求对象
request = urllib.request.Request(
    url='http://httpbin.org/get',
    headers={'User-Agent': 'Mozilla/5.0'}
)
# 2、发请求获取响应对象
response = urllib.request.urlopen(request)
# 3、获取响应对象内容
html = response.read().decode('utf-8')
code = response.getcode()
url = response.geturl()
print(html)
# 好，现在我们请求头就变成我们自己更改的了