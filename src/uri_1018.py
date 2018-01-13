"""Problem 1018 from URI Judge Online"""
# pylint: disable-msg=C0103
value = input()
bills = [100, 50, 20, 10, 5, 2, 1]
print value
for bill in bills:
    amount = value/bill
    value = value%bill
    print "{} nota(s) de R$ {},00".format(amount, bill)
