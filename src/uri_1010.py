"""Problem 1010 from URI Judge Online"""
# pylint: disable-msg=C0103
line1 = raw_input()
product1 = line1.split(" ")
line2 = raw_input()
product2 = line2.split(" ")
value = int(product1[1])*float(product1[2]) + int(product2[1])*float(product2[2])
print "VALOR A PAGAR: R$ {0:.2f}".format(value)
