# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from crapySpider.models import db_connect, IpsPool

@contextmanager
def session_scope(Session):
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
class CrapyspiderPipeline(object):
    def process_item(self, item, spider):
        return item





class IpsDataBasePipeline(object):
    """保存ip到数据库"""

    def __init__(self):
        engine = db_connect()

        self.Session = sessionmaker(bind=engine)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        a = IpsPool(ip=item["ip"],
                    port=item["port"].encode("utf-8"),
                    opacity=item["opacity"].encode("utf-8"),
                    protocol=item["protocol"].encode("utf-8"),
                    address=item["address"].encode("utf-8"),
                    crawl_time = item["crawl_time"],
                    source = item["source"].encode("utf-8"))
        with session_scope(self.Session) as session:
            session.add(a)

    def close_spider(self, spider):
        pass



class MadeInChinaPipeline(object):
    """MadeInChina"""

    def __init__(self):
        engine = db_connect()

        self.Session = sessionmaker(bind=engine)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        a = IpsPool(ip=item["ip"],
                    port=item["port"].encode("utf-8"),
                    opacity=item["opacity"].encode("utf-8"),
                    protocol=item["protocol"].encode("utf-8"),
                    address=item["address"].encode("utf-8"),
                    crawl_time = item["crawl_time"],
                    source = item["source"].encode("utf-8"))
        with session_scope(self.Session) as session:
            session.add(a)

    def close_spider(self, spider):
        pass