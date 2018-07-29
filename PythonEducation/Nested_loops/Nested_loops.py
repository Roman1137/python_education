# Вложенные циклы - это циклы, находящиеся внутри других циклов. 
# Цикл, который вложен в тело другого, называется ВНУТРЕННИМ циклом. 
# Цикл, в тело которого вложен другой цикл, называется ВНЕШНИМ циклом
#
for row in range(10):
    for column in range(30):
        print('*', end ='')
    print()
