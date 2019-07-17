import random,time

count=0
oper=['+','-','*','/']

input('타임사칙연산게임 시작')
start=time.time()

for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)

    quiz=str(a)+op+str(b)
    quiz='%d %s %d' %(a,op,b)

    print(quiz,'=')
    print(eval(quiz))
    c = int(input('정답 = '))   #소수를 입력할 때 int로는 못 받기 때문에 float로하면 된다.

    if int(eval(quiz))==c:
        print("정답!")
        count+=1
    else: 
        print("오답!")

end=time.time()
et = end - start
print("%.0f초 동안 %d개 맞음" %(et,count))