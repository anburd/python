# ищем максимальнои и второе по максимальности, повтор максаксимального игнорируется

numbers=[55, 5, -5, 55, 55, 9]
i=0
n=len(numbers)
max1=numbers[0]
max2=numbers[0]

while i < n:
  if max1 < numbers[i]:        
        max1 = numbers[i]
  i+=1    
i=0
while i < n:
    if max2==max1: 
        max2=numbers[i]
    if numbers[i] != max1:
        if max2 <= numbers[i]:        
            max2 = numbers[i]
    i+=1

#print(max1, max2)
if max1==max2:
   print("в массиве все числа одинаковы и равны ",max1) 
else:
   print(max1, max2)