# Multiple Recursion Calls
# that is in one fn have many fn .... fn():fn();fn()
# 1️⃣Fibonacci number 
# 0 1 1 2 3 5 8 13
# TC-O(2^n)
def fibonacci(n:int):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

# 2️⃣Print all subsequences

# subsequence--> contiguous or non contiguous sequence which follow the order 
# sub array--> contiguous sequence which follow the order 
# here we firstly create a new list which contain the elements 
# append element in newarr then call fn one more time 
# remove element from newarr then call fn one more time
# TC-O(2^n*(n)) SC-O(n) 
def subsequence(n:int,i:int,arr:list,newArr:list):
    if i>=n:
        print(newArr,end=" ")
        return
    newArr.append(arr[i])
    subsequence(n,i+1,arr,newArr)
    newArr.pop()
    subsequence(n,i+1,arr,newArr)

# 3️⃣Print all subsequences whose sum is k
# using sum
# TC-O(2^n) SC-O(n) 

def subsequenceK(n:int,i:int,arr:list,newArr:list,k:int):
    if i>=n:
        if sum(newArr)==k:
            print(newArr,end=" ")
        return
    newArr.append(arr[i])
    subsequenceK(n,i+1,arr,newArr,k)
    newArr.pop()
    subsequenceK(n,i+1,arr,newArr,k)


# without using sum
# TC-O(2^n) SC-O(n) 

def subsequencesK2(n:int,i:int,arr:list,newArr:list,k:int,s:int):
    if i>=n:
        if s==k:
            print(newArr,end=" ")
        return
    newArr.append(arr[i])
    s+=arr[i]
    subsequencesK2(n,i+1,arr,newArr,k,s)
    newArr.pop()
    s-=arr[i]
    subsequencesK2(n,i+1,arr,newArr,k,s)


# 4️⃣Print anyone subsequence whose sum is k
# doubt💀💀💀💀
# TC-O(2^n) SC-O(n) 
def subsequenceOneK(n:int,i:int,arr:list,newArr:list,k:int,s:int):
    if i>=n:
        if s==k :
            print(newArr,end=" ")
            return True
        return False
    newArr.append(arr[i])
    s+=arr[i]
    if subsequenceOneK(n,i+1,arr,newArr,k,s) ==True:
        return True
    newArr.pop()
    s-=arr[i]
    if subsequenceOneK(n,i+1,arr,newArr,k,s)==True:
        return True
    return False


# 5️⃣count subsequences whose sum ==k
# TC-O(2^n) SC-O(n) 
def countSubsequenceK(n:int,i:int,arr:list,newArr:list,k:int,s:int):
    if i>=n:
        if s==k:
            return 1
        return 0
    newArr.append(arr[i])
    s+=arr[i]
    l=countSubsequenceK(n,i+1,arr,newArr,k,s)
    newArr.pop()
    s-=arr[i]
    r=countSubsequenceK(n,i+1,arr,newArr,k,s)
    return l+r

     
if __name__=="__main__":
    # print(fibonacci(3))
    a=[1 ,2 ,1 ,2 ,3 ,2, 3, 4 ,4]
    # subsequence(3,0,a,[])
    # subsequencesK2(3,0,a,[],3,0)
    # subsequenceOneK(3,0,a,[],3,0)
    # print(countSubsequenceK(9,0,a,[],9,0))
    print(subsequence(9,0,a,[]))