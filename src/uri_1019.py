"""Problem 1019 from URI Judge Online"""
# pylint: disable-msg=C0103
seconds = input()
hours = seconds/60/60
minutes = seconds%3600/60
seconds = seconds%60
print "{}:{}:{}".format(hours, minutes, seconds)
