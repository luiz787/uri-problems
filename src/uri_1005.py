"""Problem 1005 from URI Judge Online"""
# pylint: disable-msg=C0103
a = input()
b = input()
A_WEIGHT = 3.5
B_WEIGHT = 7.5
average = ((a*A_WEIGHT)+(b*B_WEIGHT))/(A_WEIGHT+B_WEIGHT)
print "MEDIA = {0:.5f}".format(average)
