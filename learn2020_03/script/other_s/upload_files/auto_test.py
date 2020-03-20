"""
@Name: auto_test
@Version: 
@Project: PyCharm
@Author: wangmin
@Data: 2018/11/13
"""

import paramiko
import time

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh.connect('47.100.60.152',22,'gttest','q7TkPLVa')

# stdin, stdout, stderr = ssh.exec_command('ps -ef|grep apiteach|grep -v grep') # 查询liunx中apiteach这个进程是否运行
# stdin, stdout, stderr = ssh.exec_command('ps -ef|grep http|grep -v grep') # 查询liunx中apiteach这个进程是否运行
#
# print(stdout.read().decode('utf-8'))

host = '47.100.60.152'
port = 22
username = 'gttest'
password = 'q7TkPLVa'
class SSHConnection:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.transport = None
        self.sftp = None
        self.client = None
        self.connect()  # 建立连接
#
    def connect(self):
        transport = paramiko.Transport(self.host, self.port)
        transport.connect(username=self.username, password=self.password)
        self.transport = transport

#     # 下载
#     def download(self, remotepath, localpath):
#         if self._sftp is None:
#             self._sftp = paramiko.SFTPClient.from_transport(self.transport)
#         self._sftp.get(remotepath, localpath)
#
#     # 上传
#     def put(self, localpath, remotepath):
#         if self._sftp is None:
#             self._sftp = paramiko.SFTPClient.from_transport(self.transport)
#         self._sftp.put(localpath, remotepath)
#
#     # 执行命令
    def exec_command(self, command):
        if self.client is None:
            self.client = paramiko.SSHClient()
            #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #目的是接受不在本地Known_host文件下的主机。

            self.client.transport = self.transport
        stdin, stdout, stderr = self.client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print(data.strip())  # 打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print(err.strip()) # 输出错误结果
            return err

    def close(self):
        if self.transport:
            self.transport.close()
        if self.client:
            self.client.close()
#
#
if __name__ == "__main__":
    conn = SSHConnection('47.100.60.152',22,'gttest','q7TkPLVa')

    conn.exec_command('ls')
    # print(stdout.read().decode('utf-8'))
    # conn.exec_command('cd /home/test;pwd')  # cd需要特别处理
    # conn.exec_command('pwd')
    # conn.exec_command('tree /home/test')


