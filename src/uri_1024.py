"""Problem 1024 from URI Judge Online"""
# pylint: disable-msg=C0103
# FIXME: 100% wrong answer
cases = input()
results = []
for i in range(0, cases):
    phrase = raw_input()
    phrase = list(phrase)
    phrase = phrase[:-1]
    for key in range(0, len(phrase)):
        if phrase[key].isalpha():
            phrase[key] = ord(phrase[key])+3 #Ascii value of char+3
            phrase[key] = str(unichr(phrase[key])) #Converting back to character
    phrase = phrase[::-1]
    for key in range(len(phrase)/2, len(phrase)):
        phrase[key] = ord(phrase[key])-1
        phrase[key] = str(unichr(phrase[key]))
    results.append(''.join(phrase))
for result in results:
    print result
