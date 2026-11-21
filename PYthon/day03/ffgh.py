# 1. Таблица умножения 10×10 вложенными циклами, с выравниванием через f" {x:4}"

# for a in range(1, 11):
#     for b in range(1, 11):
#         print(f"{a * b:4}", end="")
#     print()

# 2. FizzBuzz от 1 до 100.

# for a in range(1, 101):
#   if a % 3 == 0 and a % 5 == 0:
#     print("fizzbuzz")
#   elif a % 3 == 0:
#     print("fizz")
#   elif a % 5 == 0:
#     print("buzz")
#   else:
#     print(a) 

# 3. Сумма цифр числа без преобразования в строку (через % 10 и // 10 ).

# number = int(input("Введите число: "))
# total = 0
# number = abs(number)
# while number > 0:
#   last_digit = number % 10 
#   total = total + last_digit 
#   number = number // 10 
# print("Сумма цифр", total)

# 4. Все простые числа до N; для проверки используйте for ... else .
# b = int(input("Введите число до "))
# for i in range (1, b+1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i , "Составное число")    



#Доработайте «Угадай число»: лимит в 7 попыток и предложение сыграть ещё raz

# import random
# def play_game():
#     secret = random.randint(1, 100)
#     attemps = 0
#     while attemps < 7:
#         guess = int(input("Ваше число "))
#         attemps += 1
#         if guess == secret:
#             print(f"Угадали за {attemps} попыток ")
#             break
#         elif guess < secret:
#             print("Больше")
#         else:
#             print("Меньше")
#     else:
#             print(f"Попытки закончились. Загаданное число было {secret}")        
#     answer = input("Играть заново? (y/n): ")
#     return answer.strip().lower() == "y"
# play_again = True
# while play_again:
#         play_again = play_game()

