# 1️⃣ single number I
# given an array contain every number 2 times except one number, find the number
# approach 1
# TC-O(n/2)
def singleNumberI1(arr:list):
    new=set(arr)#tc?????????????????????
    for i in new:
        if arr.count(i)!=2:
            return i


# OPTIMAL
# use xor--->xor prop--> a^a=0 and a^0=a
# TC-O(N)
def singleNumberI2(arr:list):
    x=0
    for i in arr:
        x=x^i
    return x

# 2️⃣ single number II
# given an array contain every number 3 times except one number, find the number
def singleNumberII1(arr:list):
    new=set(arr)#tc?????????????????????
    for i in new:
        if arr.count(i)!=2:
            return i
# approach 2
# TC-O(nlogn + N/3)
def singleNumberII2(s:list):
    s.sort()
    for i in range(1,len(s),3):
        if s[i]!=s[i-1]:
            return s[i-1]
    return s[len(s)-1]
# approach 3
# should know beforehand
# ----- using bit manipulation
# here one, two variables which store the occurrence of no if a no appear one time then store that in one and when second time store it in two at last we get 0 in both var
# not understand the whole... recheck💀💀💀
# TC-O(N) SC-O(1)
def singleNumberII3(arr:list):
    ones=0
    twos=0
    for i in arr:
        ones=(ones^i)&(~twos)
        twos=(twos^i)&(~ones)
    return ones




# 3️⃣ Single Number III---left💀💀💀
# given an array contain every number 2 times except two number, find the numbers
# approach 1
# TC-O(n/2)
def singleNumberIII1(arr:list):
    new=set(arr)#tc?????????????????????
    ans=[]
    for i in new:
        if arr.count(i)!=2:
            ans.append(i)
    return ans

# approach 2



if __name__=="__main__":
    a=[2,3,2,1,1,4,4]
    a1=[1,3,2,3,2,3,]
    # print(singleNumberI1(a))
    # print(singleNumberI2(a))
    # print(singleNumberII2(a1))
    a2=[2,3,4,2,4,3,5,6]
    print(singleNumberIII1(a2))