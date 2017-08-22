# mystr="Строка"+12 #Вызовет ошибку

mystr = "Строка" + str(12)  # Правильно
print(mystr)

num = 12 + 12.1  # Автоматически преобраз. в float.
print(num)
