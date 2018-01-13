"""Problem 1006 from URI Judge Online"""
# pylint: disable-msg=C0103
a = input()
b = input()
c = input()
A_WEIGHT = 2
B_WEIGHT = 3
C_WEIGHT = 5
average = ((a*A_WEIGHT)+(b*B_WEIGHT)+(c*C_WEIGHT))/(A_WEIGHT+B_WEIGHT+C_WEIGHT)
print "MEDIA = {0:.1f}".format(average)
