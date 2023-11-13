# тест
questions = [
    '1.Сколько будет 2+2?\n1)4\n2)6\n3)2',
    "2.Сколько будет 3+2?\n1)8\n2)4\n3)5",
    "3.Сколько будет 2+5?\n1)18\n2)7\n3)10",
    "4.Сколько будет 10-4?\n1)6\n2)10\n3)12",
    "5.Сколько будет 10+10?\n1)5\n2)20\n3)2"]
points=0
correctAnswers = [2,3,2,1,2]
for i in range(len(questions)):
    print(questions[i])
    answer = int(input("введите свой ответ_>"))
    if answer==correctAnswers[i]:
        points+=1
print(f"вы набрали-{points} из {len(questions)}")