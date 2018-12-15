import os
with open('text.txt', 'w+') as fp:
    fp.write("Hello world!%s" % os.linesep)
    fp.write("I'm just for test.")
l = ['I am the first']
with open('text.txt') as fp:
    l.extend(fp)
print l
