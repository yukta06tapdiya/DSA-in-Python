from collections import deque

s=input("Enter a string:")

dq=deque()

for ch in s:
    dq.append(ch)

print("Deque elements:",dq)

reversed_string=""
while dq:
    reversed_string+=dq.pop()

print("Reversed string", reversed_string)

if s==reversed_string:
    print("The string is palindrome")
else:
    print("The string is not palindrome")