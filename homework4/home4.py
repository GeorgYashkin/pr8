a=int(input())
b=int(input())
if a>b:
    while a>b+1:
        b += 1
        print(b)
else:
    while b>a+1:
        a+=1
        print(a)
