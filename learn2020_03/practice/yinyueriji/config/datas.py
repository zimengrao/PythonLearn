"""
@Name: datas
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/8/20
"""

import pymysql
from sqlalchemy import Column,DateTime,create_engine,Boolean,Integer,String,select,MetaData
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 1、创建连接
engine = create_engine("mysql+pymysql://gttest:COk+Y5.g8FDxJ5s@47.100.60.152:3306/ceshihao3.6")

Base = declarative_base()

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String(20),nullable=False)
    passwd=Column(String(50),nullable=False)
    createtime=Column(DateTime,default=datetime.now)
    _locked=Column(Boolean,default=False,nullable=False)
    #在modules中写好查询条件，使用时直接调用
    @classmethod
    def all(cls):
        return session.query(cls).all()
    @classmethod
    def by_name(cls,username):
        return session.query(cls).filter_by(username=username).all()
    @property
    def locked(self):
        return self._locked

    def __repr__(self):
        return '<User(id=%s,username=%s,passwd=%s,createtime=%s,_locked=%s)>'%(
          self.id,
          self.username,
          self.passwd,
          self.createtime,
          self._locked
        )
class UserDetails(Base):
     __tablename__='user_details'
     id=Column(Integer,primary_key=True,autoincrement=True)
     id_card=Column(Integer,nullable=True,unique=True)
     last_login=Column(DateTime)
     login_num=Column(Integer,default=0)
     user_id=Column(Integer,ForeignKey('user.id'))
#bakcref建立反向索引，
     userdetails_for_foreignkey=relationship('User',backref='details',uselist=False,cascade='all')
     def __self__(self):
         return '<UserDetails(id=%s,id_card=%s,last_login=%s,login_num=%s,user_id=%s)>'%(
             self.id,
             self.id_card,
             self.last_login,
             self.login_num,
             self.user_id
         )
if __name__=='__main__':
    Base.metadata.create_all()