
listdata=[]
while True:
    print('''
    ========== 리스트 데이터 관리 ===========
    1. 리스트에 추가    2. 리스트 데이터 수정   
    3. 리스트 데이터 삭제   4. 종료
    ''')
    menu = int(input("메뉴를 선택하세요."))

    if menu == 4:
        break

    elif menu == 1:
        data = input('추가할 데이터를 입력하세요.')
        listdata.append(data)
        print(listdata)
    elif menu == 2:
        print(listdata)
        n=int(input('뒤에서 몇번째 데이터를 수정하시겠습니까?'))
        c=input('어떻게 수정하시겠습니까?')
        listdata[-n]=c
        print(listdata)
    elif menu == 3:
        print(listdata)
        n=int(input('뒤에서 몇번째 데이터를 삭제하시겠습니까?'))
        del listdata[-n]
        print(listdata)