x = input("введите текст->")
namefile = input("введите имя файла->")
info = namefile.split(".")
if len(info)==2 and info[1].lower()=="txt" :
    file = open(namefile,"a+",encoding="utf8")
    file.write(x)
    file.close()
    print("данные успешно сохранены")
else:
    print('не правильное имя файла, данные не сохранены')