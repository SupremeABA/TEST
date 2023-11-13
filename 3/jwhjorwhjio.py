fuel=int(input("выберите марку бензина\n1.92\n2.95\n3.98\n4.DT->"))
litr=int(input("выберите кол-во литров"))
cost = 0
match fuel:
    case 1:
        cost=30*litr
    case 2:
        cost=32*litr
    case 3:
        cost=38*litr
    case 4:
        cost=39*litr
print(f"стоимость вашей запрвки->{cost}")





