# -*- coding: utf-8 -*-
import telnetlib

import requests
import scrapy
from selenium.webdriver import Proxy
from selenium import webdriver
from selenium.webdriver.common.proxy import ProxyType

from crapySpider import IPPools
from crapySpider.items import Hc360DetailItem


'''
慧聪网数据爬取
'''

class StartSpider(scrapy.Spider):
    name = "StartSpider"
    #allowed_domains = ['www.hc360.com','b2b.hc360.com']
    start_urls = [
        "http://vote1.qblife.com.cn/vote24/survey/7?from=timeline&isappinstalled=0"
    ]

    def parse(self, response):
        service_args = []
        service_args.append('--load-images=no')  ##关闭图片加载
        service_args.append('--disk-cache=yes')  ##开启缓存
        service_args.append('--ignore-ssl-errors=true')  ##忽略https错误
        browser = webdriver.PhantomJS(service_args=service_args)

        count = 0
        while 1==1:
            print(count)
            proxyIp = requests.get("http://tvp.daxiangdaili.com/ip/?tid=557895172920514&num=1&filter=on").content
            # thisip = str(IPPools.get_proxy(), encoding="utf-8")
            thisip = str(proxyIp, encoding="utf-8")

            try:
                #telnetlib.Telnet('127.0.0.1', port='80', timeout=20)

                requests.get('http://vote1.qblife.com.cn/vote24/survey/7?from=timeline&isappinstalled=0', proxies={"http": "http://"+thisip},timeout=1)
            except:
                print('connect failed')
            else:
                print('success')
                try:
                    proxy = webdriver.Proxy()
                    proxy.proxy_type = ProxyType.MANUAL
                    proxy.http_proxy = thisip
                    proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
                    browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
                    browser.get("http://vote1.qblife.com.cn/vote24/survey/7?from=timeline&isappinstalled=0")
                    browser.set_page_load_timeout(3)

                    #print(browser.page_source)
                    elem = browser.find_element_by_id("loadmore")
                    elem.click()
                    elem = browser.find_element_by_id("vote-btn-178")
                    elem.click()

                except:
                    print('获取不到元素')
                else:
                    num = browser.find_element_by_id("vote-num-178").text


                    print('点赞成功'+num)

                    count = count + 1

