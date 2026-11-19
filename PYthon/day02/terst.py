score = int(input("Баллы (0–100): "))
if score < 0 or score > 100:
    print("Некорректное значение")
elif score >= 85:
    print("Отлично")
elif score >= 60:
    print("Хорошо")
else:
    print("Нужно подтянуть")
# Цепочка сравнений и тернарный оператор
if 0 <= score <= 100:
    status = "сдал" if score >= 60 else "не сдал"
# match/case (Python 3.10+)
command = input("> ")
match command:
    case "start":
        print("Запуск")
    case "stop" | "exit":
        print("Остановка")
    case _:
        print("Неизвестная команда")