# x < y
# x > y
# x <= y
# x >= y
# x == y
# x != y

#Операции is и is not проверяют ПО РАСПОЛОЖЕНИЮ В ПАМЯТИ, а не по значению как == и !=
#т.е операции is и is not проверяют, что два объекта либо указывают либо не указывают на один и тот же объект в памяти
#ВАЖНО!! В Python к одному и тому же обьекту может быть привязано несколько разных имет - переменных
# x is y - x и y - это один и тот же объект
# x is not y - x и y не являются один и тем же обьектом памяти

#Можно использовать двойные сравнения, например -2 <= x < 3 Python автоматически вставляет между операциями 'and'

print(True and True)
condition1 = True
condition2 = False
print(condition1 and condition2)

condition2 = True
print(condition1 and condition2)

print(condition1 or False) #True
print(not condition1) #False
#Прооритет операций - сначала все, что в скобках, потом not, потом and, а потом уже or
# представь, что not - это как минус для чисел, and - умножить или поделить, а or - это добавить или отнять

condition = not True and (False or True) #выведет False т.к сначала в скобках (False or True) -> True,
#потом not True -> False, потом уже and 

print()
print(2 > 3)
print(2 < 3)
print(2 <= 4)
print(2 != -5)

print()
print(2 is 2) #создался обьект в памяти 2. второй такой же обьект Python не создает, он видит, что уже есть такой жа обьект и использует его
print("string" is "string")

variable1 = input("Введите слово 'qwerty' ")
variable2 = input("Введите слово 'qwerty' ещё раз ")
print("Хоть и значение обьектов равны, но это 2 разных обекта")
print("variable1 == variable2", variable1 == variable2)
print("varialbe1 is variable2", variable1 is variable2)
print("Адрес памяти, где распологается объект связан с variable1", id(variable1))
print("Адрес памяти, где распологается объект связан с variable2",id(variable2))

print()
a = 55
print(2 < 5 <= 100)
a=1; b=1; c=1;
print(a == b == c and a is b is c) #выводит true