#'String' и "String" - это одно и то же
#Смотреть до конца
string1 = 'String'
string2 = "String"

print(type(string1), type(string2))

#символ \ означает, что это строку мы ещё не закончили и хотим написать след. часть строки с другой строки
string = "First line of text. " \
         "Second line of text."
print(string)

string = "First line of text.  \
         Second line of text."
print(string) #все проблелы          Second line of text." теперь есть в нашей строке

string = "First line of text.\n" \
         "Second line of text."
print(string)

#чтобы вывести символы \, " или любой другой спец. символ нужно использовать \ перед каждым знаком
string = "First line of text \"" \
         "Second line of text."
print(string)

#весь формат сохраняется. Для этого можна использовать либо """ либо '''
multiline_string = """ Lesson 2. Variables and Data types
        some data types in this lesson:
-int
-bool
-float
-complex
-str
"""
print(multiline_string)
#c ''' эффект тот же
multiline_string = ''' Lesson 2. Variables and Data types
        some data types in this lesson:
-int
-bool
-float
-complex
-str
'''
print(multiline_string)

print()
#Конкатенация
print("Vasya" + "Vasya")

#Вывод элемента строки по его индексу
a = "Vasya"
print(a[2]) #вывело s

#Форматирование в стиле языка C
print('Number = %d' % 17) # %d - это целое число
print('Number = %f' % 17.2454) #%d - это дробное число
print('Number = %5.2f' % 17.2454) #здесь  4 - это общее количество символов, а 2 кол-во символов после запятой
print("Word %s = number %d" %('Vasua', 44))

print()
#Форматирование в стиле C#
print("Number = {}".format(17))
#индексы в {} можем как указывать, так и не указывать. если мы их не указываем, то они считаются по порядку
print("Number = {}, {}".format(11, 's'))
print('Number = {1}, {0}, {2}, {3}'.format(15, 15.4, 'Vasya', True))
#можем указать формат
print("Number = {:5.3f}, {}".format(111.5555, 's'))