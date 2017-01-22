# -*- coding: utf-8 -*-
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SETTINGS = {
    "template_path": os.path.join(BASE_DIR, "templates"),
    "static_path": os.path.join(BASE_DIR, "static"),
}

DB_CONNECT_STRING = 'mysql+mysqldb://%s:%s@%s/%s?charset=utf8'
DB_HOST = '172.29.152.190'
DB_USER = 'root'
DB_PWD = 'hitdcos'
DB_NAME = 'tornado_test'
# DB_HOST = '127.0.0.1'
# DB_USER = 'root'
# DB_PWD = 'lql'
# DB_NAME = 'tornado_test'

engine = create_engine(DB_CONNECT_STRING % (DB_USER, DB_PWD, DB_HOST, DB_NAME),encoding='utf-8', echo=False,pool_size=100, pool_recycle=10)
BaseModel = declarative_base()
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
