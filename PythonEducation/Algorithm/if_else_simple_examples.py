#Оператор if-else
#
#if условие:
#    блок_операторов_1
#else:
#    блок_операторов_2
#
# Здесь, если уловие истонно, выполняются операторы из первого блока, иначе - из второго.

x = float(input('Enter x value: '))

if x > 0:  # в отладчике можно менять значения переменных
    y = x ** 0.5
else:
    y = x ** 2
print(y)

name = input("Enter you name: ")

if name == "Roman":
    print("You have entred", name)
    print("This is my name too")
else:
    print("Entered name differes from mine")

#Пример каскадирования оператов ветвления
number = float(input("Enter any number you want: "))
if 0 < number < 7:
    print("Value is in range, let`s continue")
    y = 2 * number - 5
    if y < 0:
        print("Value is negative")
    else:
        if y > 0:
            print("Value is positive")
        else:
            print("y = 0")
