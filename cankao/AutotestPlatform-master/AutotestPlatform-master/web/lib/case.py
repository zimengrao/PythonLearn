# coding:utf-8
import uuid
import time
import json
from interface import *
import traceback


class Case:
    '''
    用例类，实例化参数：
        项目名project, 接口名name, 参数data, 检验参数assert_data, 
        保存参数save_data, 删除参数del_data, 准备时间pre_time,
        用例状态status
    
    工作流：
        1、通过project,name 实例化interface对象
        2、依照data去修改interface的self.params
        3、下发接口请求
        4、依照assert_data校验响应数据,刷新用例状态status
        5、保存和删除interface对象的类变量g
        
    '''
    
    def __init__(self, project, name, data=None, assert_data=None, 
                 save_data=None, del_data=None, pre_time=0, g={}, s=''):
        self.name = name
        self.g = g
        self.interface = interf(name, project, self.g)
        self.data = data
        self.assert_data = assert_data
        self.save_data = save_data
        self.del_data = del_data
        self.status = [0,0]
        self.pre_time = pre_time
        self.s = s
        
    def run(self):
        try:
            if self.pre_time:
                time.sleep(self.pre_time)
            
            if self.data:
                if not isinstance(self.data, dict):
                    self.data = json.loads(self.data)
                self.interface.modify_params(self.data)
                self.interface.params = self.data

            if self.interface.request():
                self.status[0] = 1

            if self.assert_data:
                if not isinstance(self.assert_data, dict):
                    self.assert_data = json.loads(self.assert_data)
                if self.interface.assert_response(self.assert_data):
                    self.status[1] = 1
            else:
                self.status[1] = 1 

            if self.save_data:
                self.save_data = self.save_data.replace(' ','').split(',')
                self.interface.g_push(self.save_data)
        except:
            print(traceback.format_exc())
            pass
            
        return self.name, self.status, self.interface.log_file, self.del_data
    
