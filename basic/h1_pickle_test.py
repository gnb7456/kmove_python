import random, time,pickle

w=[]
rank={}
def sortV(x):
    return x[1]

while True:
    print("1.문제열기 2.문제저장 3.타자게임 4.등수등록 5.저장하기 6.불러오기 7.문제입력")
    menu=input("메뉴를 선택하세요\n")
    if menu=='1':
        f=open('word_p.txt','rb')
        w=w+pickle.load(f)
        f.close()
    elif menu=='2':
        f=open('word_p.txt','wb')
        pickle.dump(w,f)
        f.close()
    elif menu=='3':
        n=1
        print("[타자 게임]준비되면 엔터!")
        input()
        start=time.time()
        q=random.choice(w)
        while n<=5:
            print("*문제",n)
            print(q)
            x=input()
            if q==x:
                print("통과!")
                n=n+1
                q=random.choice(w)
            else:
                print("오타! 다시도전!")
        end=time.time()
        et=end-start
        et=format(et,".2f")
        print("타자 시간 : ", et, "초")
        name=input("사용자 이름을 입력하세요.")
        rank[name]=float(et)
    elif menu=='4':
        ranklist=sorted(rank.items(),key=sortV)
        num=1
        for k,v in ranklist:
            print("%d등 %s %f" %(num,k,v))
            num=num+1
    elif menu=='5':
        f=open('basic/rank.txt','w')
        text=''
        items=rank.items()
        for k,v in items:
            text=text+k+':'+str(v)+'\n'
        f.writelines(text)
        f.close()
    elif menu=='6':
        f=open('basic/rank.txt','r')
        line=1
        while line:
            line = f.readline().replace("\n","")
            if not(line==''):
                k,v=line.split(':')
                rank[k]=float(v)
    elif menu=='7':
        word=input("문제를 입력하세요.")
        w.append(word)
    else:
        print("메뉴를 잘못 선택하셨습니다.")