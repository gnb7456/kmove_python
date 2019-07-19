import pickle

data={1:'python',2:'you'}

f=open('basic/test_p.txt','wb')
pickle.dump(data,f)
f.close()

f=open('basic/test_p.txt','rb')
data1=pickle.load(f)
f.close()

print(data)
print(data1)
print(type(data1))