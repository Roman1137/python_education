import math

x = 3.266
print("x =", x)
print("trunc(x) =", math.trunc(x)) #Вывело 3.  Просто обрасует дробную часть числа.
print("floor(x) =", math.floor(x)) #Вывело 3.  Возвращает ближайшее целое число, которое не превышает данное
print("ceil(x) =", math.ceil(x)) #Вывело 4.  Возвращает число, которое больше или равно данному числу
print() 

x = -3.266
print("trunc(x) =", math.trunc(x)) #Вывело -3.  Просто обрасует дробную часть числа
print("floor(x) =", math.floor(x)) #Вывело -4.  Возвращает ближайшее целое число, которое не превышает данное
print("ceil(x) =", math.ceil(x)) #Вывело -3.  Возвращает число, которое больше или равно данному числу
print(math.pi)
print(math.e)

print(math.sin(math.pi / 4))

print(1 / math.sqrt(2))

#Разница между math.sqrt(4) и 4 ** 0.5
d = -8;
print(d ** 0.5) #ошибки нету
print(math.sqrt(d)) #есть ошибка

