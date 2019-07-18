import random, time

count=1
tazalist=['파이썬','미국','엔지니어','교육','힘들다','매우','집','가다','원하다']
gamelist=random.choice(tazalist)

input('타자게임 시작')
start=time.time()

while(count<=5):
    print(gamelist)
    gameanswer=str(input('타자를 입력하시오. : '))
    if(gamelist == gameanswer):
        print("정답입니다.")
        count+=1
        gamelist=random.choice(tazalist)
    else:
        print("오답입니다. 다시 입력하시오. : ") 

end=time.time()
t=end-start
print('타자 시간 : {:.0f}초'.format(t))


