def add(a,b):       # a,b는 매개변수(들어오는 값을 받을 변수)
    return a+b

print(add(5,4))     # 5,4는 인수(들어오는 값)
c=add(5,6)
print(c)

def add_many(*a):       # add_many(*a,choice) 라고 하면 오류남.
    result=0            # why? *a의 갯수가 어디까지인지 몰라서 choice를 인식불가
    print(type(a))      # 오류가 안나려면? add_many(choice,*a)로 바꾸면 된다.
    print(a)
    for i in a:
        result=result+i
    return result


total=add_many(1,2,3,4,5,6,7,8,9,10)
print(total)
print()

def add_and_mul(a,b):
    return a+b,a*b


'''total=add_and_mul(3,6)       # 29-33번째 줄과 같은 내용
print(type(total))
print(total)
'''     
add,mul=add_and_mul(3,6)
print(type(add))
print(type(mul))
print(add)
print(mul)