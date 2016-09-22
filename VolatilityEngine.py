#############################
# author: patrick yang
# date: 2016-09-07
# function: different types of volatility
#############################

from sqlalchemy import create_engine

class VolCalculator:
    def __init__(self):
        self.mysql_conn_str = 'mysql://root:223223@localhost/optboy'
        self.vol_engine = create_engine(self.mysql_conn_str)
        self.conn = self.vol_engine.connect()

    def calc(self, price_df, vol_type='GARCH'):
        pass

    def get_vol(self, symbol, vol_type):
        query_str = "select * from vol_curve where symbol = '" + symbol + "' and vol_type = '" + vol_type + "'"
        print query_str
        result = self.conn.execute(query_str)
        for r in result:
            print "iv", r["iv"]
            return r["iv"]




