s=0
print("Введите числа")
while (True):
    y=input()
    if y.isdigit():
        s+=int(y)
    elif (y=="stop" or y=="end"):
        break
print("Сумма этих чисел равна",s)
