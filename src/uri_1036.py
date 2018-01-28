"""Problem 1036 from URI Judge Online"""
# pylint: disable-msg=C0103
import sys
line = raw_input()
args = map(float, line.split())
delta = args[1]**2-4*args[0]*args[2]
if delta < 0 or args[0] == 0:
    print "Impossivel calcular"
    sys.exit()
else:
    root1 = ((-1*args[1])+(delta**0.5))/(2*args[0])
    root2 = ((-1*args[1])-(delta**0.5))/(2*args[0])
    print "R1 = {0:.5f}".format(root1)
    print "R2 = {0:.5f}".format(root2)
