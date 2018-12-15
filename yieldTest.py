from itertools import islice
l = []
def foo():
    i = 0
    while True:
        yield i
        i += 1

a = foo()
print 'a.next is ', a.next
print 'a.next():', a.next()
print 'a.next():', a.next()
print 'a.next():', a.next()
print 'a.next():', a.next()

llslice = islice(a, 0, 6)
lslice = islice(a, 0, 6)
ll = list(llslice)
l.extend(lslice)
l.extend(xrange(6))
print 'll :', ll
print 'l: ', l
