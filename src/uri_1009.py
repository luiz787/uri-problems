"""Problem 1009 from URI Judge Online"""
# pylint: disable-msg=C0103
name = raw_input()
salary = input()
value_sold = input()
final_salary = salary + value_sold*15/100
print "TOTAL = R$ {0:.2f}".format(final_salary)
