# for i in range (1, 11, 2):
#     print(i, end="")

# for index, letter in enumerate("Код"):
#     print(index, letter)

# Игра угадай число

import random
secret = random.randint(1, 100)
attemps = 0
while True:
    guess = int(input("Ваше число "))
    attemps += 1
    if guess < secret:
        print("Больше ")
    elif guess > secret:
        print("Меньше ")
    else:
        print(f"Угадали за {attemps} попыток")
        break