"""Problem 1021 from URI Judge Online"""
# pylint: disable-msg=C0103
# TODO: debugar para perceber inconsistencias de floating point
import math
bills = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
value = input()
value = value*100
print "NOTAS:"
for bill in bills:
    bill = bill*100
    amount_of_bill = int(math.floor(value/bill))
    print "{} nota(s) de R$ {}.00".format(amount_of_bill, bill/100)
    value = value%bill
print "MOEDAS:"
for coin in coins:
    coin = coin*100
    amount_of_coin = int(math.floor(value/coin))
    value = value%coin
    print "{0} moeda(s) de R$ {1:.2f}".format(amount_of_coin, coin/100)
