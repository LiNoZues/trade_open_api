# -*- encoding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2024/07/25 16:29:48
@Author  :   LenoZues 
@Version :   1.0
@Contact :   chenzhe12320@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''
# here put the import lib
import yaml
from datetime import datetime
from store import US_TIMEZONE, CN_TIMEZONE
import pytz

def read_yaml(path: str):
    with open(path) as f:
        return yaml.safe_load(f)
    

def get_current_cn_time(market = 'CN'):
    # 获取当前市场的当地时间
    if market == 'US':
        us_time = datetime.now(US_TIMEZONE).time()
        return us_time
    return datetime.now().time()

def session_str2time_str(time_str: str):
    # 将session的时间字符串转换成time对象
    time_format = "%H:%M:%S"
    time_obj = datetime.strptime(time_str, time_format).time()
    return time_obj
