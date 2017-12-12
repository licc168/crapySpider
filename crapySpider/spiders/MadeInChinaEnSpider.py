# -*- coding: utf-8 -*-
import scrapy,urllib,re

from crapySpider.items import MadeInChinaItem
from scrapy.http import Request,FormRequest

'''
中国制造网英文版
'''


class MadeInChinaEnSpider(scrapy.Spider):
    name = "HcSpider"
    # allowed_domains = ['www.hc360.com','b2b.hc360.com']
    start_urls = [
        "http://www.made-in-china.com/manufacturers-directory/item3/Paint-Coating-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Foam-1.html"

    ]
    header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
    # def start_requests(self):
    #     url = "https://login.made-in-china.com/sign-in/?logonInCode=1"
    #     return [Request(url, meta={'cookiejar': 1},
    #                     callback=self.post_login)]

    def start_requests(self):
        url='https://login.made-in-china.com/sign-in/?logonInCode=1'
        return [Request(url=url,meta={"cookiejar":1},callback=self.post_login)]

    def post_login(self, response):
        print('Preparing login')

        # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数



        return [FormRequest.from_response(response,
                                          formid="logon",
                                          formdata={
                                              "logonInfo.logUserName": "1510273413@qq.com",
                                              'logonInfo.logPassword': 'jumore2017',
                                              'baseNextPage': '',
                                              'applyGTSource': '',
                                              'rembemberLoginNameFlag': "1",
                                              'jumpNext': ''
                                          },
                                          meta={"cookiejar": response.meta["cookiejar"],'dont_redirect': True, "handle_httpstatus_list": [302]},
                                          headers=self.header,
                                          callback=self.after_login
                                          )]

    def after_login(self, response):
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        for sel in response.xpath('//div[@class="search-list"]/div[contains(@class,"list-node")]'):
            href = sel.xpath('h2[@class="company-name"]/a/@href').extract()
            if len(href) > 0:
                url = response.urljoin(href[0])
                yield scrapy.Request(url, callback=self.parse_item)
                ## 是否还有下一页，如果有的话，则继续
                # next_pages = response.xpath('//div[@class="pager"]/div[@class="page-num"]/strong/following-sibling::*[1]/@href').extract()
                # if len(next_pages) > 0:
                #     page_url = response.urljoin(next_pages[0])
                #     yield scrapy.Request(page_url, callback=self.parse)

    def parse_item(self, response):
        url = response.url
        if url =='http://www.made-in-china.com/showroom/annie168moyuan/':
            tel = response.xpath("//div[@class ='info-cont-wp']/div[@ class ='item'][2]/div[@ class ='info']/text()").extract()
            tel = response.xpath('//a[@class="J-company-sign"]/text()').extract()

            print(tel)

        item = MadeInChinaItem()
        companyName = response.xpath('//div[@class="main-info"]/h3/strong/a/text()')[0].extract()

        print(response.url)
        print(companyName)
        return item
