import re,sys,pickle

class Customer:
    custlist=[]
    page=-1

    def insertData(Self):

    def curSearch(self):
    
    def preSearch(self):
    
    def nextSearch(self):
    
    def deleteData(self):

    def updataData(self):

    def quit(self):
        print("프로그램을 종료합니다.")
        sys.exit()

    def savaData(self):
        with open('basic/data.pk1','wb') as f:
            pickle.dump(self.custlist,f)

    def loadData(self):
        #파일 크기가 0보다 클 경우에 읽어옴.
        #if os.path.getsize('basic/data.pk1')>0:
        #파일이 존재할 경우에 읽어옴.
        if os.path.exists('basic/')
    
    def firstinput(self):
        choice=input()
    
    def exe(Self,choice):
        if choice=='I':
            self.insertData()
        elif 
    def __init__(Self):
        self.loadData()
        while True:
            self.exe(self.firstinput())

Customer()