"""Problem 1015 from URI Judge Online"""
# pylint: disable-msg=C0103
point1 = raw_input()
p1 = point1.split(" ")
p1 = map(float, p1)
point2 = raw_input()
p2 = point2.split(" ")
p2 = map(float, p2)
distance = pow(pow(p1[0]-p2[0], 2)+pow(p1[1]-p2[1], 2), 0.5)
print "{0:.4f}".format(distance)
