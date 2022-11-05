numbers=[55, 55, 55, 55, 55, 55]
i=0
n=len(numbers)
max1=numbers[0]
max2=numbers[0]

while i < n:
  if max1 < numbers[i]:        
        max1 = numbers[i]
    
  elif max2 < numbers[i]:
      max2 = numbers[i]
  i+=1 
print(max1, max2) 



i=0
while i < n:
    if max2==max1: 
        max2=numbers[i]
    if numbers[i] != max1:
        if max2 <= numbers[i]:        
            max2 = numbers[i]
    i+=1
print(max1, max2)