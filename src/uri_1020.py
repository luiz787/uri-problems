"""Problem 1020 from URI Judge Online"""
# pylint: disable-msg=C0103
days = input()
years = days/365
months = days%365/30
days = days%365%30
print "{} ano(s)".format(years)
print "{} mes(es)".format(months)
print "{} dia(s)".format(days)
