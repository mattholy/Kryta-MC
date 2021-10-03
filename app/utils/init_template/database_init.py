# -*- encoding: utf-8 -*-
'''
database_init.py
----
初始化数据库


@Time    :   2021/10/03 12:25:03
@Author  :   Mattholy
@Version :   1.0
@Contact :   smile.used@hotmail.com
@License :   MIT License
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()
engine = create_engine('sqlite:///kryta-system.db?check_same_thread=False')

