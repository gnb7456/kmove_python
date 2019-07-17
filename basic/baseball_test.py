import random

num=random.sample(range(1,9),3)
#print(num)
strike=0
count=0
ball=0

while(strike<3):
    strike=0
    ball=0
    mynum=input('중복되지 않는 숫자 입력 : ')
    
    if(mynum[0] == mynum[1] == mynum[2]):
        print("중복 X")
        count+=1
        continue
    elif(mynum[0] == mynum[1]):
        print("중복 X")
        count+=1
        continue
    elif(mynum[0] == mynum[2]):
        print("중복 X")
        count+=1
        continue
    elif(mynum[1] == mynum[2]):
        print("중복 X")
        count+=1
        continue
    else:
        pass
    
    for i in range(0,3):
        for j in range(0,3):
            if(num[i] == int(mynum[j]) and i == j):
                strike+=1
            elif(num[i] == int(mynum[j]) and i != j):
                ball+=1
    print(strike, "스트라이크, ", ball,"볼 ")
    count+=1
print(count,"번 만에 정답")