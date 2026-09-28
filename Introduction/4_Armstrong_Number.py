n=int(input("enter a number:"))
number_of_digits=len(str(n))
total=0
temp=n
while temp>0:
    total=(temp%10)**int(number_of_digits)+total
    temp=temp//10
print("sum of powers",total)
if total==n:
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

