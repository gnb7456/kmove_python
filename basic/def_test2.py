a=1
alist=[1,2,3]

def add_data():
    a=2
    alist.append(4)
    print("안 %d" %a)

add_data()
print("바깥쪽 %d" %a)
print(type(a))
print(type(alist))

# 기본적인 데이터 int 정수값 같은 건 다른 주소에 영역이 다르게 할당 되는데
# list나 딕셔너리 같은 것은 같은 영역에서 사용해서 
# int는 바깥쪽과 안쪽 값이 다른데
# list는 바깥쪽과 안쪽 값이 같다.
''' if) int도 바깥쪽과 안쪽 값도 같이 쓰려면 
    def add_data():
        global a
    이런 식으로 global함수로 바깥쪽 a를 안쪽으로 가져와서 사용한다.
'''