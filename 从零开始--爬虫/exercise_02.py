"""
你已经成功获取到了网站的响应，现在我们来通过不同的方式解读
"""
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com/")
# 响应对象response  中的方法
# read()得到结果为bytes数据类型
bytes = response.read()
# decode()转为string类型
string = response.read().decode
# 返回实际数据的URL地址
url = response.geturl()
# 返回HTTP响应码
code = response.getcode()
