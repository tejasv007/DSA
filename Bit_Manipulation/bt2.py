'''
Docstring for Bit_Manipulation.bt2
MATH TRICKS USING BITS MANIPULATION
# computer perform bitwise operation fast than any other operation
'''
# 1️⃣swap 2 variable
# use xor ie ^ bcoz 5^5==>0
def swapping(x:int,y:int):
    x=x^y
    y=x^y
    x=x^y
    return x,y

# 2️⃣check if the ith bit is set or not
# 13 -->1101 
# now for above if i==2 then ans be true 
# if i==1 then ans be false
# using bit manipulation--->
# use left shift operator on 1 ie 1<<k
# then use and on 13 and result get by above step
# if above result !=0 then true else false

def checkiBitOrNotL(x:int,i:int):
    a=1<<i
    ans=x&a
    if ans!=0:
        return True
    return False


# using right shift operator
# use right shift on x >>i
# then use and on the above and 1
# if res is 1 then true else false
# TC and SC-O(1)
def checkiBitOrNotR(x:int, i:int):
    new=x>>i
    if new&1==1:
        return True
    return False

# 3️⃣set the ith bit 
# if the ith bit is 0 then it to 1 but if 1 then keep it as it is
# left shift 1 by i 
# use or on x and res by above step
def setIthBit(x:int,i:int):
    return x | (1<<i)
        

# 4️⃣clear the ith bit
# if the ith bit is 1 then it to 0 but if 0 then keep it as it is
# complement the left shift 1 by i 
# use and on x and res by above step
def clearIthBit(x:int,i:int):
    return x & ~(1<<i)


# 5️⃣ toggle the ith bit
# if the ith bit is 0 then change it to 1 and vice versa
# left shift 1 by i 
# use xor on x and res by above step
def toggleIthBit(x:int,i:int):
    return x ^(1<<i)

# 6️⃣ remove the last set bit
# use n-1
# apply and to n and n-1
def removeLastSetBit(x:int):
    return x& (x-1)


# 7️⃣check no is power of 2 or not
# we know that if a no is power of 2 then if we remove last set bit it becomes 0
# above get by 6 question
def checkNoPower2(x:int):
    if x &(x-1)==0:
        return True
    return False

# 8️⃣count the no of set bits

def countNoSetBits(x:int):
    c=0
    while(x>1):
        c+=x&1
        x=x>>1

    if x==1:
        c+=1
    return c


# use 7 and use loop and a var to count the bits 
# if the no become 0 end the loop
# TC-O(no of set bits)
def countNoSetBits2(x:int):
    c=0
    while(x!=0):
        x=x&(x-1)
        c+=1
    return c
if __name__=="__main__":
    # print(swapping(3,6))
    # print(checkiBitOrNotL(13,2))
    # print(checkiBitOrNotR(13,2))
    # print(setIthBit(9,0))
    # print(clearIthBit(13,2))
    # print(removeLastSetBit(40))
    # print(countNoSetBits(13))
    print(countNoSetBits2(13))

