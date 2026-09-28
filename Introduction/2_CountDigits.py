n=int(input())
num=n
count=0
while num>0:
    count+=1
    num=num//10
print(f"NO. of digits in {n} is {count}")


#OR
from math import log10
n=int(input())
print("Number of digits in ",n,"is",int(log10(n))+1)