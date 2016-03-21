# -*- coding: utf-8 -*-

# module maths
import math

paquet = 10 * pow(10, 3)
debit = 10 * pow(10, 6)

tps_moy_serv = paquet * 1.0 / debit

for p in range(1, 100):
    p = p / 100

    lambd = p * 1.0 / tps_moy_serv
    n = p / (2 * (1 - p))
    w = 1 / (2 * (1 / tps_moy_serv - lambd))

    print(str(tps_moy_serv) + ' ' + str(lambd) + ' ' + str(n) + ' ' + str(w))
