# -*- coding: utf-8 -*-
import scrapy
import time

from crapySpider.items import IpoolItem


class KdlippoolspiderSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'crapySpider.pipelines.IpsDataBasePipeline': 300},
    }
    name = 'KdlIpPoolSpider'
    allowed_domains = ["kuaidaili.com"]
    start_urls = (
            'http://www.kuaidaili.com/free/inha/1',
            'http://www.kuaidaili.com/free/intr/1',
    )

    def parse(self, response):

        for row in response.xpath('//table//tr'):
            tds = row.xpath('td');
            if len(tds) == 7:
                item = IpoolItem()
                item['ip'] = ''.join(tds[0].xpath('text()').extract())
                item['port'] = ''.join(tds[1].xpath('text()').extract())
                item['opacity'] = ''.join(tds[2].xpath('text()').extract())
                item['protocol'] = ''.join(tds[3].xpath('text()').extract()).lower()
                item['address'] = ''.join(tds[4].xpath('text()').extract())
                item['crawl_time'] = int(time.time())
                item['source'] = self.name
                yield item
