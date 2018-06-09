#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'''
__author__:'vaca'
__description__:'发送邮件'
__mtime__:2016/6/11
'''

import yagmail
from readConfig import ReadConfig
from log import Log

ReadConfig = ReadConfig()
log = Log()

class SendEmail:
    def __init__(self):
        self.mail_host = ReadConfig.get_config("EMAIL", "mail_host")
        self.mail_user = ReadConfig.get_config("EMAIL", "mail_user")
        self.mail_pass = ReadConfig.get_config("EMAIL", "mail_pass")
        self.mail_port = ReadConfig.get_config("EMAIL", "mail_port")
        self.receiver = ReadConfig.get_config("EMAIL", 'receiver')
        self.receiver1 = ReadConfig.get_config("EMAIL", 'receiver1')
        self.subject = ReadConfig.get_config("EMAIL", "subject")
        self.content = ReadConfig.get_config("EMAIL", "content")
        self.on_off = ReadConfig.get_config("EMAIL", "on_off")

    def sendmail(self,report_address):
        '''发送邮件
            report_address: 附件报告地址
        '''
        if self.on_off == '1':
            try:
                yag = yagmail.SMTP(user=self.mail_user, password=self.mail_pass, host=self.mail_host,
                                   port=self.mail_port)
                yag.send(to=[self.receiver, self.receiver1], subject=self.subject, contents=self.content, attachments=report_address)
                log.info('邮件发送成功')
            except Exception:
                log.info('邮件发送失败')
        else:
            log.info('不发送邮件')


def main():
    SendEmail().sendmail(r'E:\myAppiumproj\request_test2\testReport\report\2017-06-11-15-03-27 report.xlsx')
if __name__ == '__main__':
    main()


