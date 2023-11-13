class Animal:
    weight = 0 # свойства, поля
    height = 0
    tipe = ""
    def __init__(self,t,w,h): # вызов констр
        self.tipe=t
        self.weight = w
        self.height = h
    def voise(self,sound): # self ссылка на текущий объект
        print(f"{self.tipe} издал  звук:{sound}")
lion = Animal("Лев",120,100)
suslik = Animal("Суслик",10,30)
lion.voise("РЫЫЫЫЫк")
suslik.voise("Писк")




