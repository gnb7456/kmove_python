a=[]
b=[1,2,3]
c=['life','is']
d=[1,2,'life']
e=[1,2,[1,2,3,]]

print(a)
print(b)
print(c)
print(d)
#print(e[3])
print(e[2][1])

print(type(e))

a=[1,2,3]
a[2]=4
print(a)

del a[1]
print(a)

a=[5,7,6,2,4,1]
a.sort(reverse=True)
print(a)

la={'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(la['name'])
print(la.keys())
