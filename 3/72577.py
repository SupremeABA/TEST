import random
class Artefacts:
    def __init__(self,p,h,m,w):
        self.power=p
        self.hast=h
        self.magic=m
        self.weight=w
    def __add__(self,other):
        if(type(other) is Artefacts):
            return Artefacts(self.power + other.power,self.hast + other.hast,self.magic+other.magic,self.weight+other.weight)
        else:
            return self

class Weapon(Artefacts):
    def __init__(self,p,s,m,w):
        super().__init__(p,s,m,w)
        self.__attack_power = p*s / w
        self.__magic_power = m*s/self.__attack_power
        self.__armor_reduction = p*w / 1000 if p*w < 800 else 0.8
        self.__critical = p*s / 1000 if p*s < 800 else 0.8
    def __add__(self,other):

        if(type(other) is Artefacts):
            if random.random()<=0.7:
                print("оружие улучшенно")
                return Weapon(self.power + other.power,self.hast + other.hast,self.magic+other.magic,self.weight+other.weight)
            else:
                print("оружие не улучшилось")
                return Weapon(self.power*0.9,self.hast*0.9,self.magic*0.9,self.weight*0.9)
        else:
            return self
    def __str__(self):
        return f"weapon:\natackpower->{self.__attack_power}\nmagicpower->{self.__magic_power}\narmorreduction->{self.__armor_reduction}\ncritical->{self.__critical}"
        
sword=Weapon(10,11,10,5)
print(sword)
art=Artefacts(5,7,4,6)
sword1=sword+art
print(sword1)



