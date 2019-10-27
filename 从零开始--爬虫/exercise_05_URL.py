# 使用模块urllib.parse,作用是给URL地址中查询参数进行编码
# 可以发现我们通过百度搜索不同的关键词时URL地址会有变化，所以将URL改成我们需要的就可以自动获取响应了。
# eg:编码前：https://www.baidu.com/s?wd=美女
# eg:编码后：https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
import urllib.parse
query_string = {'wd': '美女'}
result = urllib.parse.urlencode(query_string)
# result:'wd=%e7%be%8e%e5%a5%b3'
url = "http://www.baidu.com/s?{}".format(result)
print(url)
# 假如有多个查询参数，也是一样
query_string2 = {
    'wd': '美女',
    'pn': '50'
}
result2 = urllib.parse.urlencode(query_string2)
url2 = "http://www.baidu.com/s?{}".format(result2)
print(url2)

# 上面涉及到了URL地址的拼接方法，也可用其它方法完成url的拼接
# base_url = "http://www.baidu.com/s?"
# url = base_url + result
# url2 = base_url + result2
# url = "http://www.baidu.com/s?%s"% result
# url2 = "http://www.baidu.com/s?%s"% result2


# quote编码,与上面方法差别不大，大同小异
# url = 'http://www.baidu.com/s?wd={}'
# word = input("请输入：")
# query_string3 = urllib.parse.quote(word)
# print(url.format(query_string3))