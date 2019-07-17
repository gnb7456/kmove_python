import time

input("게임을 시작하려면 엔터키를 눌러주세요.")
start=time.time()
input("속으로 20초를 카운트하고 엔터키를 입력하세요.")
end=time.time()
et=int(end-start)
print("실제시간 : ", et, "초")
print("차이 : ", abs(et - 20), "초")