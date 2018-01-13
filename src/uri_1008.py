"""Problem 1008 from URI Judge Online"""
# pylint: disable-msg=C0103
number = input()
worked_hours = input()
hour_value = input()
salary = worked_hours*hour_value
print "NUMBER = {}".format(number)
print "SALARY = U$ {0:.2f}".format(salary)
