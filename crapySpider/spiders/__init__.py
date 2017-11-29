# -*- coding: utf-8 -*-
import scrapy



class HcSpider(scrapy.Spider):
    name = "HcSpider"
    allowed_domains = ['www.hc360.com']
    start_urls = [
        "https://www.hc360.com/"
    ]

    def parse(self, response):
        print 11111111111111111111111111