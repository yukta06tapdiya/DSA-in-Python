#parameterszied and functional recursion
#sum of n numbers 
# TC-O(n) in worst case
# SC-O(n)
def func(sum,i,n):
    if i>n: 
        print(sum)
        return -1
    func(sum+i,i+1,n)
func(0,1,10)

def f(n):
    if n==1: 
        return 1
    return n + f(n-1)
a=f(10)
print(a)