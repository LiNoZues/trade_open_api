# -*- encoding: utf-8 -*-
'''
@File    :   quote.py
@Time    :   2024/07/25 18:09:38
@Author  :   LenoZues 
@Version :   1.0
@Contact :   chenzhe12320@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''
from longport.openapi import Config,QuoteContext
# here put the import lib
class Quote:
    def __init__(self,config: Config) -> None:
        self.ctx = QuoteContext(config)
        self.session = self.ctx.trading_session()['MarketTradingSession']
    
    def get_market_session_info(self,market:str):
        if market == 'US':
            for item in self.session:
                if item['market'] == 'US':
                    return item
    
    def get_current_market_trade_session(self,market:str):
        if market == 'US':
            inof = self.get_current_market_trade_session(market)
            
                    
        