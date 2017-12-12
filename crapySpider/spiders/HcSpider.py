# -*- coding: utf-8 -*-
import scrapy



from crapySpider.items import Hc360DetailItem


'''
慧聪网数据爬取
'''

class HcSpider(scrapy.Spider):
    name = "HcSpider"
    allowed_domains = ['www.hc360.com','b2b.hc360.com']
    start_urls = [
        "https://www.hc360.com/"
    ]

    def parse(self, response):
         for sel in response.xpath('//div[@class="tabConList"]/ul/li/dl/dd'):
            href = sel.xpath('a/@href').extract()
            if len(href)>0:
                url = response.urljoin(href[0])
                #print ("parse_url>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"+url)
                yield scrapy.Request(url, callback=self.parse_list)
            #return item

    def parse_list(self, response):
        for sel in response.xpath('//div[@class="pro_list"]/ul/li'):
            href = sel.xpath('div[@class="picmid"]/a/@href').extract()
            if len(href) > 0:
                url = response.urljoin(href[0])
                yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        item = Hc360DetailItem()
        title = response.xpath('//h1[@id="comTitle"]/text()')[0].extract()
        item['url'] = response.url
        item['title'] = title

        return item
