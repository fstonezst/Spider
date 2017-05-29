# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector


class NgaSpider(scrapy.Spider):
    # 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    name = "NgaSpider"

    host = "http://bbs.ngacn.cc/"

    # start_urls是我们准备爬的初始页
    # 包含了Spider在启动时进行爬取的url列表。
    # 因此，第一个被获取到的页面将是其中之一。
    # 后续的URL则从初始的URL获取到的数据中提取。
    start_urls = [
        "http://bbs.ngacn.cc/thread.php?fid=406",
    ]

    # 这个是解析函数，如果不特别指明的话，scrapy抓回来的页面会由这个函数进行解析。
    # 对页面的处理和分析工作都在此进行，这个示例里我们只是简单地把页面内容打印出来。
    # 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response
    # 对象将会作为唯一的参数传递给该函数。该方法负责解析返回的数据(response data),
    # 提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    def parse(self, response):
        selector = Selector(response)
        print(response.body)
