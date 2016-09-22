from OptionEngine import *
import unittest
from VolatilityEngine import VolCalculator

from datetime import date,datetime

# date01 ="2016-09-01"
# d1 = datetime.strptime(date01, "%Y-%m-%d")
# print d1


# vc = VolCalculator()
# vc.get_vol("rb1610", "long")

oc = OptionCalculator("zn1611", "call", "long", 19800.0, 17867.0, "2016-09-10", "2016-10-11", 5500)
oc.calc_greeks(oc.r, oc.D, oc.t, oc.strike, oc.settle_price, oc.d1, oc.d2, oc.sigma, oc.quantity)
oc.calc_opt(oc.r, oc.D, oc.t, oc.d1, oc.d2, oc.settle_price, oc.strike, oc.option_direction, oc.quantity, 'BS')



import math
# from numpy import *
# from time import time
#
# random.seed(20000)
# t0 = time()
#
# S0 = 100
# K = 105
# T = 1.0
# r = 0.05
# sigma = 0.2
# M = 50
# dt = T / M
# I = 250000
#
# S = S0 * exp(cumsum((r - 0.5 * sigma ** 2) * dt + sigma * math.sqrt(dt) * random.standard_normal((M+1,I)), axis=0))
# S[0] = S0
#
# print maximum(S[-1]-K,0)
#
# C0 = math.exp(-r * T) * sum(maximum(S[-1]-K,0)) / I
#
# tpy = time() - t0
# print "European Option Vlue %7.3f" % C0
# print "Duration in Seconds %7.3f" % tpy




