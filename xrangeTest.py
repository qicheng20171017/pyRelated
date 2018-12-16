l = []
a = xrange(10000)
b = iter(a)
print b.next()
l.extend(a)
print l[0]
print 'l.len:', len(l)
