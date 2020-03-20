"""
@Name: mysql_data
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/6/12
"""

import pymysql
import logging
from config.cnf import Config

class MysqlData(Config):
    def __init__(self):
        super(MysqlData, self).__init__()
        self.config = Config()
        self.mysql_config = {
            'host': self.config.get_config('MYSQL', 'hostname'),
            'user': self.config.get_config('MYSQL', 'user'),
            'passwd': self.config.get_config('MYSQL', 'password'),
            'db': self.config.get_config('MYSQL', 'db'),
            'port': int(self.config.get_config('MYSQL', 'port')),
            'charset': self.config.get_config('MYSQL', 'charset'),
        }

    def connect(self):
        try:
            self.conn = pymysql.connect(**self.mysql_config)
            return self.conn

        except pymysql.Error:
            logging.error('connect to ' + self.mysql_config.get('host') + ' Failed')
            logging.exception('exception message:')
            return False

    def selectOne(self, sql):
        logging.info('Execute sql: ' + sql)
        self.conn = self.connect()
        self.cur = self.conn.cursor()

        try:
            self.cur.execute(sql)
            self.cur.close()
            self.conn.commit()
            self.result = self.cur.fetchone()
            # print(self.result)
            return self.result
        except Exception as err:
            self.conn.rollback()
            raise err
        finally:
            self.cur.close()

    def selectAll(self, sql):
        logging.info('Execute sql: ' + sql)
        self.conn = self.connect()
        self.cur = self.conn.cursor()

        try:
            self.cur.execute(sql)
            self.cur.close()
            self.conn.commit()
            self.result = self.cur.fetchall()
            # print(self.result)
            return self.result
        except Exception as err:
            self.conn.rollback()
            raise err
        finally:
            self.cur.close()

    def delete(self, sql):
        logging.info('Execute sql: ' + sql)
        self.conn = self.connect()
        self.cur = self.conn.cursor()

        try:
            self.cur.execute(sql)
            self.cur.close()
            self.conn.commit()
            self.result = self.cur.fetchone()
            # print(self.result)
            return self.result
        except Exception as err:
            self.conn.rollback()
            raise err
        finally:
            self.cur.close()

# if __name__ == '__main__':
#     data = MysqlData()
#     data.delete("delete FROM gt002_user_auth WHERE tc002_name='021-66316066'")
    # data.connect()
