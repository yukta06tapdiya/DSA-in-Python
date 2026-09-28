#print numbers from 1 to n using head recursion
def func(i,n):
    if i>n:
        return -1
    print(i)
    func(i+1,n)
func(1,20)

#print numbers from n to 1 using tail recursion
def func(i,n):
    if i>n:
        return -1
    func(i+1,n)
    print(i)
    
func(1,20)