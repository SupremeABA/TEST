import random
def cube ():
    com = [random.randint(1,6) for i in range(2)]
    print(f"компьютер выкинул-{com}")
    print("нажмите ENTER")
    input()
    user = [random.randint(1,6) for i in range(2)]
    print(f"вы выкинули-{user}")
    if sum(com)>sum(user):
        print("победил компьютер")
    elif sum(com)<sum(user):
        print("вы победили")
    else:
        print("ничья")
while True:
    cube()
    x=input(" нажмите ENTER для продолжения или 0 для завершения->")
    if x == "0":
        break

        
    



     