# Цикл while
#
# while условие: 
#       операторы
#
# Блок операторов не может быть пустым. Если такая необходимость возникает, можно
# вопользоваться оператором pass, который не делает ничего
#
# Блок операторов выполняется до тех пор, пока условие продолжения цикла истинно. 
# Если же оно изначально было ложным, то он не выполнится ни разу

#while True:
#    pass

response = '';

while (response != "exit"):
    response = input("Type 'exit' to exit: ")

#while not (response != "exit"):       # в Python вместо ! нужно использовать not
#    response = input("Type 'exit' to exit: ")

while True:
    pass