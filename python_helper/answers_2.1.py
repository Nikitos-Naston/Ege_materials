# ЛЕГКО
# (1) Знак числа: ввод n → "Положительное/Ноль/Отрицательное"
n = int(input("Введите число: "))
if n > 0:
    print("Положительное")
elif n == 0:
    print("Ноль")
else:
    print("Отрицательное")

# (2) Количество цифр в числе: через str или деление // 10
# 1 var
n = int(input())
c = 0
while n > 0:
    n = n //10
    c += 1
print(c)

# 2 var 
n = input()
c = 0
for char in n:
    c += 1
print(c)

# СРЕДНЕ
# (3) FizzBuzz: 1..n — "Fizz" кратно 3, "Buzz" кратно 5, "FizzBuzz" кратно 15
n = int(input("n: "))
for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

# (4) Максимум из k чисел: без встроенного max()
n = int(input())
maxi = 0
for i in range(n):
    x = int(input())
    if maxi < x:
        maxi = x
print(maxi)

# СЛОЖНО
# (5) Проверка простоты: делители до sqrt(n)
n = int(input())
find = False
for i in range(2, n // 2):
    if n % i == 0:
        find = True
if find:
    print("Не простое")
else:
    print("Простое")
# (6) Угадай число: загаданное 1..100, подсказки "больше/меньше", счётчик попыток
import random 
hidden_number = random.randint(1,100)

numb = int(input())
count = 0
while hidden_number != numb:
    if numb > hidden_number:
        print("Меньше")
    else:
        print("Больше")
    count += 1
    numb = int(input())
print(f"Угаданно за {count} попыток")

# (7) Банкомат: разложить сумму на 5000/2000/1000/500/200/100 (минимум купюр)
n = int(input())
money_5000, money_2000, money_1000, money_500, money_200, money_100, = 0,0,0,0,0,0
money_5000 += n // 5000
n = n % 5000
money_2000 += n // 2000
n = n % 2000
money_1000 += n // 1000
n = n % 1000
money_500 += n // 500
n = n % 500
money_200 += n // 200
n = n % 200
money_100 += n // 100
print(f"5000 : {money_5000} \n2000 : {money_2000} \n1000 : {money_1000} \n500 : {money_500} \n200 : {money_200} \n100 : {money_100}")
