s=0
print("Введите числа")
while (True):
    y=input()
    if (y=="stop" or y=="end"):
        break
    elif y.isalpha():
        print("Ошибочно введено число")
    else:
        s+=float(y)

print("Сумма этих чисел равна",s)
