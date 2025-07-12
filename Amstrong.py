n=int(input())
temp=n
list1=[]
sum1=0
while n>0:
    n1=n%10
    list1.append(n1)
    n=n//10
for i in list1:
    sum1+=i**3
if sum1==temp:
    print(f"{temp} is Amstrong number")
else:
    print(f"{temp} is not an Amstrong number")