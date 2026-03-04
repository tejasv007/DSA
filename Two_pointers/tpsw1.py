# 1️⃣ maximum points you can obtain from k cards✅  checked
# but you chose the 4 continous from start or from end--> for eg
# k=4 then choose 3 from front and 1 from back 
# arr=[6,2,3,4,7,2,1,7,1] k=4 ans=16(by choosing 6+2 and 7+1 2 from front and two from back )
# tc O(2k)
def maxSumKCards(arr:list,k:int):
    n=len(arr)
    ls=sum(arr[:k])
    rs=0
    l=k-1
    r=n-1
    m=ls
    while(r>(n-k)):
        ls-=arr[l]
        l-=1
        rs+=arr[r]
        r-=1
        m=max(m,ls+rs)
    return m


# 2️⃣longest substring without repeating characters
# s=cadbzabcd  ans =5
# substring similar to subarray--> contigious string
# 1. brute force
# find all substring and count the string
# tc O(n²) 
def longestSubstringWithoutRepeat(s:str):
    l=len(s)
    m=-1
    for i in range(l):
        a=""
        for j in range(i,l):
            if s[j] in a:# tc?
                m=max(m,len(a))
                break
            a=a+s[j]
    return m


# 2. optimal checked✅
# using sw and two ptrs
# here we use dict store the character and their index
# expand r, if get char which is already in dict then change the l to dict char value +1 and also change the char value
# TC O(n) sc O(n)
def longestSubstringWithoutRepeat2(s:str):
    l=0
    r=0
    ll=len(s)
    d=dict()
    i=0
    m=-1
    while(r<ll):
        if s[r] in d.keys():
            if d[s[r]]>=l:
                l=d[s[r]]+1
        d[s[r]]=i
        m=max(m,r-l+1)
        r+=1
        i+=1
    return m


# 3️⃣ max consecutive ones 111
# a=[1,1,1,0,0,0,1,1,1,1,0] k=2 ans 6
# find the len of max consecutive one and only flip out k no of zeroes to one
# we can assume this question as longest subarray with at most k zeroes

# 1 brute force approach  checked✅
# here generate all subarray and get the len 
# tc O(n²) sc O(1)
def maxConsecutiveOnesIII(arr:list,k :int):
    m=-1
    l=len(arr)
    for i in range(l):
        kNo=0
        for j in range(i,l):
            if kNo==k:
                m=max(m,(j-i+1))
                break
            if arr[j]==0:
                kNo+=1
            m=max(m,(j-i+1))
    return m

# 2 optimal approach---is good  checked✅
# here we use sw and tp approach and use a var name zeroes which store the zeroes
# if zeroes >k then increase the l till zeroes get equal to k
# tc O( 2n )
def maxConsecutiveOnesIII2(arr:list, k:int):
    l=0
    r=0
    m=-1
    zeroes=0
    ll=len(arr)
    while(r<ll):
        if arr[r]==0:
            zeroes+=1
        if zeroes>k:
            while(l<r):
                if arr[l]==0:
                    zeroes-=1
                l+=1
        else:
            m=max(m,r-l+1)
        r+=1
    return m

# 3 most optimal 
# use second pattern third one 
# O(n)
def maxConsecutiveOnesIII3(arr:list,k:int):
    l=0
    r=0
    m=-1
    zeroes=0
    ll=len(arr)
    while(r<ll):
        if arr[r]==0:
            zeroes+=1
        if zeroes <=k:
            m=max(m,r-l+1)
        else:
            if arr[l]==0:zeroes-=1
            l+=1
        r+=1
    return m


# 4️⃣FRUITS INTO BASKETS

if __name__=="__main__":
    arr=[6,2,3,4,7,2,1,7,1]
    k=4
    # print(maxSumKCards(arr,k))
    s="cadbzabcd"
    # print(longestSubstringWithoutRepeat2(s))
    a=[1,1,1,0,0,0,1,1,1,1,0]
    k=2
    print(maxConsecutiveOnesIII3(a,k))
