"""Problem 1012 from URI Judge Online"""
# pylint: disable-msg=C0103
input_line = raw_input()
vals = input_line.split(" ")
a = float(vals[0])
b = float(vals[1])
c = float(vals[2])
PI = 3.14159
triangle = a*c/2
circle = PI*pow(c, 2)
trapezium = ((a+b)*c)/2.0
square = pow(b, 2)
rectangle = a*b
print "TRIANGULO: {0:.3f}".format(triangle)
print "CIRCULO: {0:.3f}".format(circle)
print "TRAPEZIO: {0:.3f}".format(trapezium)
print "QUADRADO: {0:.3f}".format(square)
print "RETANGULO: {0:.3f}".format(rectangle)
