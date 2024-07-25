# -*- encoding: utf-8 -*-
'''
@File    :   store.py
@Time    :   2024/07/25 16:38:03
@Author  :   LenoZues 
@Version :   1.0
@Contact :   chenzhe12320@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''
# here put the import lib
import os
import locale
from longport.openapi import Config,Language
import pytz


app_key = 'e4704fe2f9a4b35d8d92032ab49796f4'
app_secret = '28b2c5b59c42db2707fb6fa1a1510a0e168bf9ac45085b680ddcb3268bbeae81'
access_token = 'm_eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJsb25nYnJpZGdlIiwic3ViIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzI5NjcyMTMwLCJpYXQiOjE3MjE4OTYxMzEsImFrIjoiZTQ3MDRmZTJmOWE0YjM1ZDhkOTIwMzJhYjQ5Nzk2ZjQiLCJhYWlkIjoyMDM1NjkzMiwiYWMiOiJsYl9zZyIsIm1pZCI6ODc4OTc4Nywic2lkIjoicTlPNG1qVDlNRTNxZkxWS0J4QmpwQT09IiwiYmwiOjMsInVsIjowLCJpayI6ImxiX3NnXzIwMzU2OTMyIn0.thFBRa-v0SfDExIS_5TX_sr4XZPNV9KXYgSRIH3MNkTmeFhRRfALLsSnd-Q70vTjudRvwZ5i8jm6-Vjgr8aoJ1Ol-Dezejh9cwQ6jueGwtcxlVtMW0Lt5M-r_zoIXH3MRPL1FL89_gAtr8Fv6NmgsYKVYsh2RCkMYdoMSj2LuEPfOEAJVLi3e_vSkokw7w5RVT5onGOwvT-Hx32k1U86ZtCkkXW0uR3oamsc9uqo8AJxQXUV6qY6X1Y2q1acYahCMdPJsWhtGbUPGyD1UZDudJgtes9JekQLzeF-QnRPOdStSxKm-X6kq29MV_XtKKEKo57woPMUGp8z76AkH4too7eHxWX3xpxiyawsr7PY54ZkATRJcC9dN-tO6dfnSlFzuM1VUYtzeQScLLMYBQzqDPFkmpLCjjuWhiuusaxuPUaVFy3mjvbCwhtbkiyn0vOO2223yr4vipv5KS3idnZwmvlKM8uCl_v33RJkvz1E4RyocTHeQ53FggE7hJjG5tncg_bIBf7Jj5RXMEpgcCemnpQamdwAzDj78TZY9qGqO1waCwxqPs6dLrCgxolVIo7nMN3GnPOhyMX8lfFKHvFCIOxCq7tKp6m8megudOc6j8xOVRHD8BN5JAuEsp1_l3ZDWPe-MC4Hqe6hyOEyeMx7NbxzAC2mHcVSlwBcM9laJW8'
enable_overnight = True

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # 把带','的数字转换成 正常的数字
base_dir = os.path.dirname(os.path.abspath(__file__))
author_config = os.path.join(base_dir, 'config.yaml')  # 用户信息


config = Config(app_key=app_key,app_secret=app_secret,access_token=access_token,enable_overnight=enable_overnight,language=Language.ZH_CN) # openapi config
US_TIMEZONE = pytz.timezone('America/New_York')
CN_TIMEZONE = pytz.timezone('Asia/Shanghai')


if __name__ == '__main__':
   
    from longport.openapi import QuoteContext
    ctx = QuoteContext(config)

    resp = ctx.trading_session()
    print(resp)