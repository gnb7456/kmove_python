'''
f = open('basic/test.txt','w',encoding='utf8')

for i in range(1,11):
    data='%d번째 줄입니다.\n'%i
    f.write(data)
    
f.close()
'''

'''f = open('basic/test.txt','r',encoding='utf8')
line = f.readline().replace('\n','')
print(line,end='')
print(type(line))
f.close()

f = open('basic/test.txt','r',encoding='utf8')
line = f.readlines()
print(line,end='')
print(type(line))

for i in line:
    print(i.repalce('\n',''))

f.close()
'''

f=open('basic/test.txt','a',encoding='utf8')
for i in range(11,20):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()