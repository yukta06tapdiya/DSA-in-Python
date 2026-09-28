#recursion using parameter
def func(x,n):
    if n==0:
        return -1
    print(x)
    func(x,n-1)

func(2,5)