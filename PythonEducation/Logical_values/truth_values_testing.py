string = input("Enter a string: ")

#if string != '':
#    print("The string is {}".format(string))

# это то же самое
if string:
    print("The string is {}".format(string))


number = int(input("Enter an integer: "))
#if number != 0:
#     print("The number is not zero")
#else:
#    print("The number is zero")

# это то же самое
if number:
     print("The number is not zero")
else:
    print("The number is zero")

#ну, на самом деле нужно смотреть по ситуации:
if string is not None and string != '':
    pass
#так читабельнее
if string:
    pass
