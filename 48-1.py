def Calc(x,y):
    print(f"{x} + {y}= {x + y}")
    print(f"{x} - {y}= {x - y}")
    print(f"{x} * {y}= {x * y}")
    if y != 0 :
        print(f"{x} + {y}= {x + y}")

while True:
    a, b = eval(input("2개의 숫자를 입력 : "))
    if b== 0 :
        break
print(Calc(a,b))

