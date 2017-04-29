#!/usr/bin/env python3

from genvec import *
from heir_lstm import *
# from ast import literal_eval
import numpy as np

bad=[1006,113,127,136,1421,1593,1603,1723,1726,1731,1751,1753,1758,1765,1767,1780,1781,1805,1813,1814,1826,1828,1829,1840,1843,1849,1851,1863,1871,1884,1885,1887,1889,1932,1936,1937,1938,193,1947,1954,1955,1973,1988,1990,1992,1994,2004,2009,2025,2042,2043,2044,2047,2057,2059,2060,2062,2065,2066,2073,2080,2089,2093,2094,2118,2122,2129,2130,2131,2135,2136,2139,2140,2143,2147,2150,2163,2164,2167,2169,2170,2175,2187,2194,2196,2202,2224,228,229,242,269,284,33,349,351,353,360,362,369,375,385,391,42,488,511,512,54,578,590,596,637,704,728,793,800,808,809,848,853,881,888,903,990,994,30,186,279,367,429,439,467,535,678]

for i in range(679,training_set_size+1):
    if i in bad:
        continue
    print("Filename:",i)
    headline, newslist = read_vectors_for_model(i)
    print(len(newslist))
    for news in newslist:
        model.fit(news, headline, epochs=nep)

model.save('test_model.h5')
