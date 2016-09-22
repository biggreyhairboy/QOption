#############################
# author: patrick yang
# date: 2016-09-07
# function: calculate value and greeks of a European Option
#############################


from math import log, sqrt, exp, pi
from scipy import stats
from datetime import datetime,timedelta
from VolatilityEngine import VolCalculator


class OptionCalculator:
    def __init__(self, symbol, option_direction, option_type, strike, underlying_price, begin_date, end_date, quantity, model='BS', r=0.06):
        self.option_direction = option_direction
        self.option_type = option_type
        self.strike = strike
        self.settle_price = underlying_price
        self.begin_date = begin_date
        self.end_date = end_date
        self.model = model
        self.r = float(r) / 244.0
        self.D = log(1 + r * 365 / 244)
        self.d1 = 0
        self.d2 = 0
        self.quantity = quantity
        self.isupdated = False
        self.sigma = self.get_sigma(symbol, option_direction, option_type)
        self.t = float(self.calc_duration(end_date, begin_date))
        self.update_d1_d2(self.r, self.t, self.sigma, self.settle_price, self.strike)


    def calc_opt(self, r, D, t, d1, d2, underlying_price, strike, option_direction, quantity, model='BS'):
        print "model " + str(model)
        option_value = 0
        #todo: change volatility for diffrent strike prices
        if model == "BS":
            if option_direction == "call":
                option_value = underlying_price * exp(-D * t) * stats.norm.cdf(d1) - strike * exp(-D * t) * stats.norm.cdf(d2)
            elif option_direction == "put":
                option_value = - underlying_price * exp(-D * t) * stats.norm.cdf(-d1) + strike * exp(-D * t) * stats.norm.cdf(-d2)
            print "option_value = " + str(option_value * quantity)
            return option_value * quantity

    def update_d1_d2(self, r, t, sigma, settle_price, strike):
        print sigma
        if self.isupdated:
            return
        else:
            self.d1 = (log(settle_price / float(strike)) + (r + 0.5 * float(sigma) ** 2) * t) / (sigma * t ** 0.5)
            #self.d2 = (log(settle_price / float(strike)) + (r - 0.5 * float(sigma) ** 2) * t) / (sigma * t ** 0.5)
            self.d2 = self.d1 - sigma * t ** 0.5
            #todo: d2 can deduct from d1
        print "d2 = " + str(self.d1)
        print "d2 = " + str(self.d2)

    def get_sigma(self, symbol, option_direction, option_type):
        vc = VolCalculator()
        sigma = 0
        if option_type == "long":
            sigma = vc.get_vol(symbol, option_type)
        elif option_type == "short":
            sigma = vc.get_vol(symbol, option_type)
        print "sigma = " + str(sigma)
        return sigma

    def calc_greeks(self, r, D, t, underlying_price, strike, d1, d2, sigma, quantity):
        print "r = " + str(r)
        print "D = " + str(D)
        print "t = " + str(t)
        delta = exp(-D * t) * stats.norm.cdf(d1)
        gamma = exp(-D * t) * stats.norm.pdf(d1) / sigma/ underlying_price
        theta = sigma * underlying_price * exp(-D * t) * stats.norm.pdf(d1) / (2 * sqrt(t)) + D * underlying_price * stats.norm.cdf(d1) * exp(-D * t) - D * strike * exp(-D * t) * stats.norm.cdf(d2)
        vega = underlying_price * sqrt(t) * exp(-D * t) * stats.norm.pdf(d1)
        rho = -t * underlying_price * exp(-D * t) * stats.norm.pdf(d1)
        greeks_names = ("delta", "gamma", "vega", "theta", "rho")
        greeks = (delta * quantity, gamma * quantity, vega * quantity, theta * quantity, rho * quantity)
        for n, g in zip(greeks_names, greeks):
            print n + " = " + str(g * quantity)

    def calc_duration(self, begin_date, end_date, tradingdays = 244.0):
        datefmt = "%Y-%m-%d"
        bdate = datetime.strptime(begin_date, datefmt)
        edate = datetime.strptime(end_date, datefmt)
        duration = edate - bdate
        print "duration = " + str(duration)
        #return duration
        #return abs(duration.days) / tradingdays
        return 56.87 / tradingdays


