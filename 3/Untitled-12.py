class Phone:
    brand = ""
    number = ""
    contacts = []
    def __init__(self,b,n):
        self.brand=b
        self.number=n
    def call(self,num):# 
        result=None
        for phone in self.contacts:
            if phone.number==num:
                result=phone
                break
        if result!=None:
            phone.incomingCall(self)
        else:
            print("номер не найден")
    def incomingCall(self,phon):
        print(f"входящий вызов:{phon.number}")
        print('1-принять\n2-отклонить')
        while True:
            x = input("->")
            if x=="1":
                print("вызов принят")
                break
            elif x=="2":
                print("вызов отклонен")
                break
phone1=Phone("Nokia","6466435")
Phone2=Phone("Samsung","7464345")
phone1.contacts=[Phone2]
phone1.call("76565654676")
            

