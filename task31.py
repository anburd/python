# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


num = int(input("Введите натуральное число N: "))

# две следующие функции нашел в интернете:

# def primfacs(n):
#     i = 2 
#     primfac = []
#     while i * i <= n:
#        while n % i == 0:
#            primfac.append(i)
#            n = n / i
#        i = i + 1
#     if n > 1:
#        primfac.append(n)
#     return primfac

# def func_search(n):
   
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             n /= i
#             yield i
#         else:
#             i += 1

#     if n > 1:
#         yield n

# первую версию переделал по-своему

def func_search(number):
    result = []

    for i in range(2, number):
        while number % i == 0:
            number /= i
            result.append(i)
    return result



print(f"Простые множители числа {num} приведены в списке: {list(func_search(num))}")