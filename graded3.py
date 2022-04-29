a = [1,2,3]
print(type(a))
b = a + [7, 8]
print(type(b))
c = {}
print(type(c))
d = 'abc-abd'
print(type(d))
e = 'abc' in d
print(type(e))
f = b.extend(a)
print(type(f))
g = b.sort()
print(type(g))
h = {1,2,3}
print(type(h))
i = h <= {2,3,4}
print(type(i))
j = d.split('-')
print(type(j))
k = b[1:4]
print(type(k))
l = h - h
print(type(l))
m = k.pop(0)
print(type(m))
o = {'john': 123456, 'jim': 343434}
print(type(o))
p = o['jim']
print(type(p))
q = len(o)
print(type(q))
#r = o['mary']