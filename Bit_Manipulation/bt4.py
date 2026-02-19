# 1️⃣ XOR of numbers till the given number
# given n a number find xor of 1 to n i.e. 1^2^3^4^5 if n=5
# approach 1
# tc o(n)
def xorNum1(n:int):
    ans=0
    for i in range(1,n+1):
        ans=ans^i
    return ans

# approach 2
# tc O(1)
# pattern-->
# n%4==1-->1
# n%4==2-->n+1
# n%4==3-->0
# n%4==0-->n 
def xorNum2(n:int):
    if n%4==0:
        return n
    if n%4==1:
        return 1
    if n%4==3:
        return 0
    return n+1

# 2️⃣  XOR of numbers in given range that is from l to r
# use xorNum 
# tc O(1)
def xorNumRange(l:int,r:int):
    return xorNum2(r)^xorNum2(l) 

# 3️⃣ Divide two integer without division and multiplication operator, find the quotient ----💀💀💀left
# approach 1
# use addition
# def divideTwoInt(divi:int,divisor:int):
    