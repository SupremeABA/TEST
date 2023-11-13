import random
class Character:
    def __init__(self,h,a,c,b,ab):
        self.hp=h
        self.atack=a
        self.crytical=c
        self.block=b
        self.ability=ab
        self.imunity=False
    def shot(self,pers2):
        try:
            if pers2.imunity:
                print("у противника иммунитет")
                pers2.imunity=False
                return 0
            totalatack=0
            match random.randint(1,3):
                case 1:
                    totalatack=self.atack
                    print("атака мечом")
                case 2:
                    totalatack=self.atack*0.7
                    print("атака кинжалом")
                case 3:
                    totalatack=self.atack
                    self.imunity=True   
                    print("магическая атака")     
            if random.random()<=self.crytical/100:
                totalatack*=2
            if random.random()<=pers2.block/100:
                totalatack/=2
            if random.random()<=pers2.ability/100:
                totalatack=0
            pers2.hp-=totalatack
            return totalatack
        except Exception as err:
            print(err)
            return 0
pers1 = Character(350,30,25,41,20)
pers2 = Character(340,41,29,33,15)
while  True:
    totalAtack = pers1.shot(pers2)
    print (f"первы персонаж наносит урон-{totalAtack}-здоровье второго перс-{pers2.hp}")
    if pers2.hp<=0:
        print(f"первый персонаж победил")
        break
    totalAtack=pers2.shot(pers1)
    print (f"второй персонаж наносит урон-{totalAtack}-здоровье первого перс-{pers1.hp}")
    if pers1.hp<=0:
        print(f"песонаж два победил")
        break
    input( "нажмите любую клавишу")
       
