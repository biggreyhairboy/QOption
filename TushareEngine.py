#############################
# author: patrick yang
# date: 2016-09-07
# function: Download daily minute open, high, low, close, volume data from tushare library
#############################

import pandas as pd
from sqlalchemy import create_engine
import tushare as ts

df = ts.get_hist_data('150195')
df.drop()
engine = create_engine('mysql://root:223223@localhost/tushare')
df.to_sql('hist_data', engine, if_exists='append')

#我记得是可以拿期货的日数据的
#区分hist_data 于日内的data


class TushareDriver:
    mysql_conn_str ='mysql://root:223223@localhost/tushare'

    def __init__(self):
        pass

    def download(self, symbol, begin_date, end_date):
        pass

