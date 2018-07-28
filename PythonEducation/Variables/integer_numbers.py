print(type(53435345345345)) #выводит int
print(type(-22324234234)) #выводит int

print(0b11101) #двоичная система счиления - выведет 29
print(0o753) #восьмеричная система счисления - выведет 491
print(0x129) #16 - ричная система счисления - выведет 297

number_as_string = "15" #попробовать number_as_string = "15a"
print(type(number_as_string))

number= int(number_as_string) #конвертируем str в int
print(type(number+999))

#Bool - значения True и False обязательно пишутся С БОЛЬШОЙ БУКВЫ
true_bool_variable = True; #True - это именованная константа значения 1
print(int(true_bool_variable)) #выведет 1
false_bool_variable= False; #False - это именованная константа значения 0
print(int(false_bool_variable)) #выведет 0

print(type(true_bool_variable)) #выведет bool
print(type(false_bool_variable)) #выведет bool

print(5+True) #ошибки НЕТУ потому, что True - это 1
print(5+False) #ошибки НЕТУ потому, что False - это 0


