numbers=[1, 2, 3, 4, 5, 6]
i=0
n=len(numbers)
j=n-1
print(i, j)
while i<j:
    tmp=numbers[i]
    numbers[i]=numbers[j]
    numbers[j]=tmp
    print(numbers[j])
    i=i+1
    j=j-1
print(numbers)