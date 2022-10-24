# import datetime

# f=(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()

# f=int(f)

# #print(f)

# def myrandint( start,end,seed=999999999	):

#     a = 32310901 # Сгенерированное случайное число является наиболее равномерным

#     b=1729

#     rOld=seed

#     m=end-start

#     while True: # Каждый раз, когда вызывается эта функция myrandint, случайное 
#         rNew = start + (a*rOld+b)%m

#         yield rNew	

#         rOld=rNew

# # Симулировать, используя 20 различных семян для генерации случайных чисел 
# for i in range(5):

#     r = myrandint(1,100, f + i)

# # Генерировать 10 случайных чисел на семя 
# print ('Seed', i, 'Generate Random Number') 
# for j in range(10):

#     print( next(r),end=',' ) 

# print(	)

# print(sum(map(int, list("".join(с for с in input("введите число: ") if с.isdecimal())))))
# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             num = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Какое-то неправильное число!")
#     return num




# import math
# a = int(input("Введите значение a= "))
# b = int(input("Введите значение b= "))
# c = int(input("Введите значение c= "))
# D = b ** 2 - 4 * a * c
# print(D)
# if D < 0:
#   print("Корней нет")
# elif D == 0:
#   x = -b / 2 * a
#   print (x)
# else:
#   x1 = (-b + math.sqrt(D)) / (2 * a)
#   x2 = (-b - math.sqrt(D)) / (2 * a)
#   print(x1)
#   print(x2)

# n = int(input("Введите значение n= "))

# factorial  = lambda x: x if x == 1 else x * factorial(x - 1) 

# print([factorial(i) for i in range(1, n + 1)])



# def get_factorial(n):
   
#     num = 1
#     for i in range(1, n + 1):
#       num *= i
#       yield num

# ls=list(get_factorial(n))

# print(ls)

# from math import gcd
 
# for a, b in (15, 30), (5, 6), (1, 0), (12, 111), (25, 60):
#     print(gcd(a, b))

import os
os.system("cls")

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "Вы выиграли!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")