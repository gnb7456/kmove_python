import random

count=0
oper=['+','-','*','/']
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

print("5개 중 %d개 맞음" %count)