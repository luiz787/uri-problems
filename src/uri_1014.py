"""Problem 1014 from URI Judge Online"""
# pylint: disable-msg=C0103
distance = input()
spent_fuel = input()
average_consumption = float(distance)/spent_fuel
print "{0:.3f} km/l".format(average_consumption)
