"""Problem 1017 from URI Judge Online"""
# pylint: disable-msg=C0103
time = input()
avg_speed = input()
distance = time*avg_speed
fuel_spent = distance/12.0
print "{0:.3f}".format(fuel_spent)
