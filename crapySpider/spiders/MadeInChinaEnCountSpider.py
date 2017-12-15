# -*- coding: utf-8 -*-
import scrapy,urllib,re
import re
'''
中国制造网英文版
'''

class MadeInChinaEnCountSpider(scrapy.Spider):
    name = "MadeInChinaEnCountSpider"
    #allowed_domains = ['login.made-in-china.com','made-in-china.com']
    start_urls = [
        # 化工数据统计
        # "http://www.made-in-china.com/manufacturers-directory/item3/Foam-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Plastic-Polymer-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Plastic-Products-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Rubber-Rubber-Products-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Paint-Coating-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Pigment-Dye-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Additive-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Chemical-Auxiliary-Catalyst-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Agricultural-Chemicals-1.html",
        # "http://www.made-in-china.com/manufacturers-directory/item3/Fertilizer-1.html"
        #工业品
        "http://www.made-in-china.com/manufacturers-directory/item3/Car-Light-Auto-Mirror-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Car-Accessories-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Fastener-Fitting-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Auto-Engine-Structure-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Auto-Parts-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Crank-Mechanism-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Abrasive-Grinding-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Diamond-Tools-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Drilling-Tools-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Hand-Tools-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Horticulture-Gardening-Products-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Power-Tools-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Building-Hardware-1.html",
        "http://www.made-in-china.com/manufacturers-directory/item3/Hardware-Accessories-1.html",
        "http://www.made-in-china.com/Tools-Hardware-Catalog/Machine-Hardware.html"




    ]

    def parse(self, response):
        max_pages_num = response.xpath('//div[@class="pager"]/div[@class="page-num"]/a[last()-1]/text()').extract()
        max_num = re.sub('\s','',max_pages_num[0])
        count = int(max_num)*30
        print(count)

