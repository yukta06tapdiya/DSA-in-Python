def palindrome(n,left,right):

    #base case
    if left<=right:
        return True
    if n[left] != n[right]:
        return False
    return palindrome(n,left+1,right-1)

def pali(n):
    return palindrome(n,0,len(n)-1)


if __name__ == "__main__":
    n = "abba"
    
    if pali(n):
        print("true")
    else:
        print("false")

    