import os
# write test file
with open('test1.txt', 'w+') as fp:
    for i in range(12):
        fp.write('%s%s' % (i, os.linesep))

con = (k for k in open('test1.txt') if '1' not in k)
print con.next()

