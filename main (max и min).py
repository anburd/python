numbers=[5, 55, 10, 4, 5, 6]
i=0
n=len(numbers)
max=numbers[0]
min=numbers[0]
while i<n:
    if numbers[i]>max:
         max=numbers[i]
    if numbers[i]<min:
         min=numbers[i]
    i=i+1
print(max)
print(min)