x = 2
y = 8 #Когда наводим на y или x(на имя переменной) - показывается тип числа

result = x + y
print(result)

print(x + 3)
print(x - y)
print()
print(x * y)
print(x / y) #возвращает число типа float
print(x // y) #возвращает число типа int (но, есть x или y - float, то и результат будет float)
print(8.0 // 4) #вывелось 2.0, хотя мы использовали //

print(x % 8) #выведет 2 - как остатот от деления т.к у нас не получилось поделить 2 на 8 и 2 осталось в остатке
print(8 % 3) #выведет 2
print(8.1 % 3) #выведет 2.099999999999

print()
print(2 ** 8)
print(2 ** 0.5)
print(pow(2,8))

print

z = -2
print(abs(z)) #выводит 2

print()

print(3.2 * 0.8 - 2 * 5 - 3 ** 3)
print()

number = 3.26
print(round(number), round(number, 1)) #выводит 3 3.3