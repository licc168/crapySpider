# -*- coding: utf-8 -*-
import scrapy

import time

from crawler import Request
from selenium import webdriver
from crapySpider.config import ZhiHuConfig # 爬虫配置


class ZhuHuSpider(scrapy.Spider):
    name = "ZhuHuSpider"
    start_urls = [
        "https://www.zhihu.com/"
    ]



    def get_cookies(self):
        driver = webdriver.Chrome()
        driver.get( 'https://www.zhihu.com/signin')
        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys(ZhiHuConfig.email)
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys(ZhiHuConfig.password)
        elem = driver.find_element_by_css_selector("SignFlow-submitButton").click()
        elem.click()
        time.sleep(2)
        cookies = driver.get_cookies()
        driver.close()
        return cookies

    # def after_login(self, response):
    #     cookies =  self.get_cookies(self)
    #     for url in self.start_urls:
    #         yield Request(url, cookies = cookies)






    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get('https://www.zhihu.com/signin')
        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys(ZhiHuConfig.get("email"))
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys(ZhiHuConfig.get("password"))
        elem = driver.find_elements_by_tag_name().click()
        elem.click()
        time.sleep(2)
        cookies = driver.get_cookies()
        driver.close()
        print(1111)






