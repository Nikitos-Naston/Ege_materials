# 6.1 Чёт/нечёт:
# n = int(input())
# print("Чётное" if n % 2 == 0 else "Нечётное")

# 6.2 Мини‑калькулятор:
# a = float(input("a: "))
# b = float(input("b: "))
# op = input("Операция (+,-,*,/): ")
# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     if b == 0:
#         print("Деление на ноль!")
#     else:
#         print(a / b)
# else:
#     print("Неизвестная операция")

# 6.3 Сумма 1..n (for):
# n = int(input("n: "))
# s = 0
# for i in range(1, n + 1):
#     s += i
# print(s)

# 6.4 Таблица умножения для k:
# k = int(input("k: "))
# for i in range(1, 11):
#     print(f"{k} x {i} = {k*i}")

# 6.5 Пароль до "python":
# tries = 0
# while True:
#     tries += 1
#     p = input("Пароль: ")
#     if p == "python":
#         print("Готово за попыток:", tries)
#         break