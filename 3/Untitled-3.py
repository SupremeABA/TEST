# найти средне арифметич
def avg(*args):
    total = 0
    for i in args:
        total+=i#
    return total/len(args)#
print(avg(25,20,47,12,13))