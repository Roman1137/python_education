#Оператор if
#if условие:
#    операторы  - никаких фигурных скобок. только отступы(рекомендуется делать отступ в 4 пробела) 
# 
# Блок операторов не может быть пустым. Если такая необходимость возникает, можно 
# воспользоваться оператором pass, которые не делает ничего
# 
# Можно использовать однострочную форму, но она не желательна
# if условие: оператор; оператор;

number = int(input("Enter a number: "))

if number> 5:
    print("The number {} is greater than five".format(number))

if number is not None:
    pass # TODO: add some logic here later