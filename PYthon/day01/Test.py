name = "Иван" # Имя #тип str
age = "25" # Возраст # тип - int
height = 1.82 # Рост # тип - float
is_student = True # Условие - являеться ли переменная учеником # тип - bool
nothing = None # Ничего # тип - None
#
#
print(type(age)) 
print(f"{name}, {age}, {height:.2f} м, {is_student}")
#
#
years = int(input("Год рождения: "))
print(f"Вам примерно {2026 - years} лет")
#
#