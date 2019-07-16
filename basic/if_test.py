money = True
if money:
    print("택시")
else:
    print("걸어감")

#조건부표현식
jumsu=int(input("성적을 입력하세요 : "))
message=''
print(jumsu)

if jumsu <=25:
    message = "F"
elif jumsu <=50:
    message = "C"
elif jumsu <= 75:
    message = "B"
elif jumsu <=100:
    message = "A"

print(message)

print('입력한 성적은 %d 입니다.' %jumsu)
print('당신의 학점은 {}입니다.' .format(message))

#print('입력한 성적은 ',jumsu,' 입니다.')    #,jumsu, 콤마로 구분자를 사용하였다.
#print('입력한 성적은 %s 입니다.', %jumsu) #%jumsu =format함수이다.

