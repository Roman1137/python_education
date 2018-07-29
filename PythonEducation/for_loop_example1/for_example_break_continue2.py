for attempts_left in range(3,0, -1):
    password = input("Enter password, "
                    "(attempts left {}) ".format(attempts_left))
    if password == '98eaxc':
        print("Access granted")
        break
else:
     print("Access denied")


print("-------")

for i in range(5): #вывело 0, 1, 2, 4, 4
    if i == 3:
        i += 1
    print(i)

#Дело в том, что как бы мы не меняли значение нашей переменной i во время одной итерации,
#из range() будет получено НОРМАЛЬНОЕ, НЕ ИЗМЕНЕННОЕ значение
#По этому, как бы мы ее не меняли, мы не можем повиять на выполнение цикла и на кол-во итераций