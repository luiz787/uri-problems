"""Problem 1013 from URI Judge Online"""
# pylint: disable-msg=C0103
input_line = raw_input()
values = input_line.split(" ")
values = map(int, values)
maiorAB = (values[0]+values[1]+abs(values[0]-values[1]))/2
maior = (maiorAB+values[2]+abs(maiorAB-values[2]))/2
print "{} eh o maior".format(maior)