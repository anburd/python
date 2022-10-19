# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


num = InputNumbers("Введите натуральное число N: ")

i = 2 # первое простое число


def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
    if n > 1:
       primfac.append(n)
    return primfac




def func_search(num):
    rezult = []

    for i in range(2, num):
        while num % i == 0:
            num /= i
            rezult.append(i)
    return rezult

print(f"Результат деления: {func_search(num)}")
print(f"Простые множители числа {old} приведены в списке: {lst}")