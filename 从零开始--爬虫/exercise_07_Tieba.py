"""
接下来玩真的，我们来爬取百度贴吧
"""
from urllib import request, parse
import time
import random
from fake_useragent import UserAgent
# python 库，提供各种User-Agent


class Tieba_Spider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'

    # 获取
    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    # 解析（此处先不解析）
    def parse_html(self):
        pass

    # 保存
    def write_save(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    # 入口函数
    def run(self):
        name = input("请输入贴吧名：")
        begin = int(input('请输入起始页：'))
        end = int(input('请输入终止页：'))

        # 查询参数编码
        params = parse.quote(name)
        for page in range(begin, end+1):
            # URL拼接
            pn = (page-1)*50
            url = self.url.format(params, pn)

            # 调用函数进行页面抓取+ 保存
            filename = '{}-第{}页.html'.format(name, page)
            html = self.get_html(url)
            self.write_save(filename, html)

            # 控制爬取速度
            time.sleep(random.randint(1, 3))
            print('第%d页抓取成功'% page)


if __name__ == '__main__':
    start = time.time()
    spider = Tieba_Spider()
    spider.run()
    end = time.time()
    print('执行时间：%.2f'% (end-start))