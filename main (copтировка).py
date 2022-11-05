numbers=[5, 55, 10, 100, 4, 6]
i=0
n=len(numbers)
k=n-1
while k>0:
    while i<n-1:
        if numbers[i]>numbers[i+1]:
             tmp=numbers[i]
             numbers[i]=numbers[i+1]
             numbers[i+1]=tmp
        i=i+1
    i=0
    k=k-1      
print(numbers)
print(numbers[-1])