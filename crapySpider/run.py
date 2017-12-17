# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc : 
"""

import logging

from crapySpider.spiders.MadeInChinaEnCountSpider import MadeInChinaEnCountSpider
from crapySpider.spiders.KdlIpPoolSpider import KdlippoolspiderSpider
from crapySpider.spiders.MadeInChinaEnSpider import MadeInChinaEnSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from crapySpider.models import db_connect


if __name__ == '__main__':
    settings = get_project_settings()
    configure_logging(settings)
    runner = CrawlerRunner(settings)
    db = db_connect()
    #runner.crawl(KdlippoolspiderSpider)
    runner.crawl(MadeInChinaEnSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    # blocks process so always keep as the last statement
    reactor.run()
    logging.info('all finished.')
