is_ready = False

if is_ready:
    state_msg = "Ready"
else: 
    state_msg = "Not ready yet"

print(state_msg)

#ОЧЕНЬ ВАЖНО
print(False or 5) #Выведет 5. Потому, что операция or в Python работает так: 
# если первое значение истинное - то операция or возвращет первое значение, если нет , то второе 
# И НЕ ВАЖНО КАКОЕ ВТОРОЕ ЗНАЧЕНИЕ!

print(True and 5) # Выведет 5. Потому, что операция and в Python работает так:
# если первое значение ложное - возвращается первое значение, если нет, то второе
# И НЕ ВАЖНО КАКОЕ ВТОРОЕ ЗНАЧЕНИЕ!

print(bool(0)) #False
print(bool(5)) #True

is_ready= False
x = is_ready and "Ready" or "Not ready yet"  #ЭТО аналог тернарного оператора в Python 2
print(x) #Выведет "Not ready yet" потому, что:
#сначала операция and(у нее больше приоритета чем в or) => вернется False(cмотри выше почему)
#потом операция or => вернется "Not ready yet"(смотри выше почему)

