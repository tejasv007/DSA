# 1️⃣ NUMBER OF SUBSTRINGS CONTAINING ALL 3 CHARACTERS
# s=bbacba
# string contain only 3 characters. find the no of substrings containing all 3 characters
# 1 brute force 
# find out all substring, build a var, contain no of substring and an arr contain all distinct char
# if arr len get 3 then add len of s - current index then break
# tc O(n²) sc O(3)
def numberSubstring3Chars(s:str):
    m=0
    ll=len(s)
    for i in range(ll):
        arr=[]

        for j in range(i,ll):
            if s[j] not in arr:
                arr.append(s[j])
            if len(arr)==3:
                m+=(ll-j)
                break
    return m

# 2. optimal one 
# here we use 3 var which store the updated index of a,b,c
# then with the traversal we update the var
# to calculate the no of substring we use min(a,c,b)+1 if all there are not -1
# that is a b c are firstly assign to -1
# tc O(n) 
def numberSubstring3Chars2(s:str):
    a=b=c=-1
    m=0
    r=0
    ll=len(s)
    while(r<ll):
        if s[r]=='a':
            a=r
        elif s[r]=='b':
            b=r
        else:c=r
        if a>-1 and b>-1 and c>-1:
            m+=(min(a,b,c)+1)
        r+=1
    return m


# 2️⃣LONGEST REPEATING CHARACTER REPLACEMENT
# S="AABABBA" K=2
# find the longest substring have all the char same, k is no times you can change one char to another 
# s can contain any char but are in all caps
# 1 brute force
# generate all substrings
# use formula len- max==k the len will be the max one
# TC O(N²) sc O(26)
# use dict store char freq and here len is subtring len and max is the largest freq 
def longestRepeatCharReplace(s:str,k:int):
    ll=len(s)
    m=-1
    for i in range(ll):
        d=dict()
        for j in range(i,ll):
            if s[j] not in d:
                d[s[j]]=1
            else:
                d[s[j]]+=1
            if (j-i+1)-max(d.values())<=k:
                m=max(j-i+1,m)
            else:break
    return m

# 2 optimal
# use sw and tp
# use l and r and d then 
# check len by r-l+1 and substract the max count if it is <=k then update m
# if >k then update l till get <=k
# tc O(2n) sc O(26)
def longestRepeatCharReplace2(s:str,k:int):
    l=0
    r=0
    ll=len(s)
    d=dict()
    m=-1
    while(r<ll):
        if s[r] not in d:
            d[s[r]]=1
        else:
            d[s[r]]+=1
            if ((r-l+1) - max(d.values())) <=k:
                m=max(m,(r-l+1))
            else:
                while(((r-l+1)-max(d.values()))>k):
                    d[s[l]]-=1
                    l+=1
        r+=1
    return m

# 3 optimal more one 
# here we use the optimal one but here we dont use inner while loop
# as we dont want to decrease the sliding window
# tc O(n) sc O(26)

def longestRepeatCharReplace3(s:str,k:int):
    l=0
    r=0
    ll=len(s)
    d=dict()
    m=-1
    while(r<ll):
        if s[r] not in d:
            d[s[r]]=1
        else:
            d[s[r]]+=1
            if ((r-l+1) - max(d.values())) <=k:
                m=max(m,(r-l+1))
                
            else:
                # while(((r-l+1)-max(d.values()))>k):
                d[s[l]]-=1
                l+=1
        r+=1
    return m

# 3️⃣NUMBER OF BINARY SUBARRAYS WITH SUM K 
# a=[1,0,1,0,1] goal =2
# here first we find the subarrays have sum<=k
# how can we know no of subarrays--> the length of subarray tell the no of subarray
# for [1,0,0,1,1,0] g=2 and sum<=k the no of subarray =1+2+3+4+4+5
# here we got to know that---> for sum==goal===> (a,k)-(a,k-1)--->not understand💀💀💀💀
# tc O(4n) sc O(1)
def numberBinarySubarraySumKHelper(a:list,k:int):
    l=0
    r=0
    ll=len(a)
    s=0
    no=0
    if k<0:return 0
    while(r<ll):
        s+=a[r]
        if s<=k:
            no+=(r-l+1)
        else:
            while(s>k):
                s-=a[l]
                l+=1
            no+=(r-l+1)
        
        r+=1
    
    return no
            

def numberBinarySubarraySumK(a:list,goal:int):
    return numberBinarySubarraySumKHelper(a,goal)-numberBinarySubarraySumKHelper(a,goal-1)


# 4️⃣COUNT NUMBER OF NICE SUBARRAYS
# nums=[1,1,2,1,1] k=3
# find the count of number of subarrays  where the sum of odd no of element is equal to k
# here we convert this problem to 3 one -- by using modulo with each element when add to s
# tc O(4n) sc O(1)

def countNumberOfNiceSubarraysHelper(a:list,k:int):##have tc O(2n) sc O(n)
    l=0
    r=0
    ll=len(a)
    s=0
    no=0
    if k<0:return 0
    while(r<ll):    
        s+=(a[r]%2)
        if s<=k:
            no+=(r-l+1)
        else:
            while(s>k):
                s-=(a[l]%2)
                l+=1
            no+=(r-l+1)
        
        r+=1
    
    return no

def countNumberOfNiceSubarrays(a:list,k:int):
    return countNumberOfNiceSubarraysHelper(a,k)-countNumberOfNiceSubarraysHelper(a,k-1)


# 5️⃣SUBARRAYS WITH EXACTLY K DIFFERENT INTEGERS💀💀💀💀💀💀approach giving different answers
# find the no of subarrays which have exactly k different integers 
#A=[1,2,1,3,4] k=3  
# 1.brute force
# build all subarrays and check all element are diff or not by using set in python and map in other language
# TC O(N²) sc (count it)
def subarraysWithExactlyKDiffInt(a:list,k:int):
    no=0
    l=len(a)
    for i in range(l):
        for j in range(i,l):
            s=set(a[i:j+1])
            if len(s)==k:
                no+=1
                break
    return no

# 2. optimise
# use sw and tp 
# problem--> dont know expand or shrink
# here we use 4 one approach find <=k no of subarrays
# find the <=k - <=(k-1)
# TC O(4N) sc O(2N)

def subarraysWithExactlyKDiffIntHelper(a:list,k:int):#have tc O(2n) sc O(n)
    l=0
    r=0
    ll=len(a)
    d=dict()
    m=0
    while(r<ll):
        if a[r] not in d:
            d[a[r]]=1
        else:
            d[a[r]]+=1
        if len(d.keys())<=k:
            m+=(r-l+1)
        else:
            while(len(d.keys())>k):
                d[a[l]]-=1
                if d[a[l]]==0:
                    d.pop(a[l])
                l+=1
            m+=(r-l+1)
        r+=1
    return m

def subarraysWithExactlyKDiffInt2(a:list,k:int):
    return subarraysWithExactlyKDiffIntHelper(a,k)-subarraysWithExactlyKDiffIntHelper(a,k-1)



# 6️⃣ MINIMUM WINDOW SUBSTRING
# s="ddaaabbca" t="abc" ans="bca"
# but if t="abbc" and ="bbca"
# find the minimum length substring have all letter which is in t 
# 1. brute force
# generate all substring and check if it fulfill the constraint or not
# here we use a dict which store data about char which is in t
# then while traversing the whole s we substract the value of the key (everytime do substraction)
# while substracting if it get 0 then make the c+=1( here c do store the len of diff char in t)
# if c==len of diff char in t then m = the string
# TC O(N²) sc (2N)

from collections import Counter
def minimumWindowSubstring(s:str,t:str):
    m=s
    l=len(s)
    d=Counter(t)
    noReq=len(d.keys())
    for i in range(l):
        d=Counter(t)
        ns=''
        c=0
        for j in range(i,l):
            ns=ns+s[j]
            if s[j] not in d.keys():
                d[s[j]]=-1
            else:
                d[s[j]]-=1
                if d[s[j]]==0:
                    c+=1
            if c==noReq:
                if len(m)>len(ns):
                    m=ns
                    break

    return m


# 2. optimal
# here we build a d counter of t, a var count the diff element(if it reach to d.keys()) then update the m(ans)
# update r till reach to var ==d.keys() then increase the l 
# when the var<d.keys() move the r 
# tc O(2n) sc O(26)
def minimumWindowSubstring2(s:str,t:str):
    l=0
    r=0
    ll=len(s)
    d=Counter(t)
    c=0
    m=s
    noReq=len(d.keys())
    while(r<ll):
        if s[r] not in d.keys():
            d[s[r]]=-1
        else:
            d[s[r]]-=1
            if d[s[r]]==0:
                c+=1
            if c==noReq:
                if (r-l+1)<len(m):
                    m=s[l:r+1]
                while(c==noReq):
                    d[s[l]]+=1
                    if d[s[l]]>0:
                        c-=1
                    if (r-l+1)<len(m):#doubt(cause striver dont use it but i use it)
                        m=s[l:r+1]
                    l+=1          
        r+=1
    return m

if __name__=="__main__":
    # s="bbacba"
    # print(numberSubstring3Chars2(s))
    s="AABABBA"
    # print(longestRepeatCharReplace3(s,2))
    a=[1,0,0,1,1,0]
    # print(numberBinarySubarraySumK(a,2))
    a1=[1,1,2,1,1]
    # print(countNumberOfNiceSubarrays(a1,3))
    A=[1,2,1,3,4] 
    a2=[2,1,1,1,3,4,3,2]
    # print(subarraysWithExactlyKDiffInt(a2,3))  
    # print(subarraysWithExactlyKDiffInt2(A,3))
    # print(subarraysWithExactlyKDiffInt2(a2,3))

    # print(subarraysWithExactlyKDiffIntHelper(a2,2))
    s="ddaaabbca" 
    t="abbc" #ans="bca"
    print(minimumWindowSubstring(s,t))
    print(minimumWindowSubstring2(s,t))
    # aaa=s[:3]
    # print(aaa)
