class Account:
    def __init__(self,login,psassword):
        self.__login=login
        self.__password=psassword
        self.__init=False
        self.__bank=0
    @property # деккоратор
    def login(self):
        return self.__login
    @property
    def bank(self):
        return self.__bank
    def setPass (self,value):
        if self.__init:
            self.__password=value
    def authorization(self,login,passw):
        if login.lower()==self.__login.lower() and passw==self.__password:
            self.__init=True
        return self.__init
    def transaction(self,value):
        if not self.__init:
            return False
        if value<0 and self.__bank+value<0:
            return False
        else:
            self.__bank+=value
            return True
    @bank.setter
    def bank (self,value):
        if not self.__init:
            return 
        if value<0 and self.__bank+value<0:
            return 
        else:
            self.__bank=value
            return 


ac = Account("Super","12345")
ac.transaction(10000)
ac.bank+=10000
print(ac.bank)
while True:
    l  = input("введите логин->")
    p = input("введите пароль->")
    if ac.authorization(l,p):
        break
    else:
        print("вы ввели неправильный логин или парооль")
ac.transaction(10000)
ac.bank+=10000
print(ac.bank)

        
               



    