n=int(input("Enter a number: "))
num=n

result=0
i=0
while num>0:
    result=(result*10)+(num%10)
    num=num//10
    
print("The reversed number :" ,result)
if result==n:
    print("It is palindrome")
else:
    print("It is not palindrome")

