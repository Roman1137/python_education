# Оператор ветвления с несколькими условиями

#if условия1:
#    операторы1
#elif условие2:
#    операторы2
#elif условие3:
#    операторы3
#...
#else:
#    операторыN

#Как и в операторе ветвления с одним условием, ветка else не является обязательной

x = float(input("x = "))
if 0 < x < 7:
    print("The value is in the range, let`s continue")
    y = 2 * x -5
    if y < 0:
        print("y is negative")
    elif y > 0:
        print("y is positive")
    else:
        print("y = 0")
