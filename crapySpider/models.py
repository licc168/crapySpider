#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 定义数据库模型实体
Desc : 
"""
import datetime

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from crapySpider.settings import DATABASE


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(DATABASE)


def create_news_table(engine):
    """"""
    Base.metadata.create_all(engine)


def _get_date():
    return datetime.datetime.now()

Base = declarative_base()


class IpsPool(Base):

    __tablename__ = 'ips_pool'

    id = Column(Integer, primary_key=True)

    ip = Column(String(30))

    port = Column(String(100))

    opacity = Column(String(100))

    protocol = Column(String(100))

    address = Column(String(200))

    crawl_time = Column(String(200))

    source = Column(String(100))







