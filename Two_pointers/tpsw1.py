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
            while(zeroes>k):
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


# 4️⃣FRUITS INTO BASKETS--> max length of subarray with at most k type of fruits  
# arr=[3,3,3,1,2,1,1,2,3,3,4]
'''There is only one row of fruit trees on the farm, oriented left to right. An integer array called fruits represents the trees, where fruits[i] denotes the kind of fruit produced by the ith tree.
The goal is to gather as much fruit as possible, adhering to the owner's stringent rules:
1) There are two baskets available, and each basket can only contain one kind of fruit. The quantity of fruit each basket can contain is unlimited.

2) Start at any tree, but as you proceed to the right, select exactly one fruit from each tree, including the starting tree. One of the baskets must hold the harvested fruits.

3) Once reaching a tree with fruit that cannot fit into any basket, stop.
Return the maximum number of fruits that can be picked.'''
# 1  brute force
# generate all subarrays
# tc O(n²) 
def fruitIntoBaskets1(arr:list):
    ll=len(arr)
    m=-1
    for i in range(ll):
        for j in range(i,ll):
            new=set(arr[i:j+1])
            if len(new)==2:
                m=max(m,j-i+1)
    return m

# 2.  optimal one 
# sw tp
# TC O(2n) sc o(3)---tc of dict💀check it out
# here we use a no which count the distinct no, dict which work as hashmap
# move r till reach ll then update no and dict according to the arr[r]
# if no>2 then move l till the len of dict key==2 
# find the m by max(m,r-l+1)
def fruitIntoBaskets2(arr:list):
    l=0
    r=0
    no=0
    m=-1
    ll=len(arr)
    no_of=dict()
    while(r<ll):
        if arr[r] in no_of.keys():
            no_of[arr[r]]+=1
        else:
            no_of[arr[r]]=1
            no+=1
        if no>2:
            while((len(no_of.keys())>2)):#doubt why no l<r
                no_of[arr[l]]-=1
                if no_of[arr[l]]==0:
                    no-=1
                    no_of.pop(arr[l])
                    break
                l+=1
            l+=1
        else:
            m=max(m,r-l+1)
        r+=1
    return m


# 3. optimal more one
# similar to first but here we dont decrease the sw according to no
# stay constant till get more len than the m
# tc O(n) sc O(3)
def fruitIntoBaskets3(arr:list):
    l=0
    r=0
    no=0
    m=-1
    ll=len(arr)
    no_of=dict()
    while(r<ll):
        if arr[r] in no_of.keys():
            no_of[arr[r]]+=1
        else:
            no_of[arr[r]]=1
            no+=1
        if no>2:
            if((len(no_of.keys())>2)):
                no_of[arr[l]]-=1
                if no_of[arr[l]]==0:
                    no-=1
                    no_of.pop(arr[l])
                #     break
                # l+=1
            l+=1
        else:
            m=max(m,r-l+1)
        r+=1
    return m



# 5️⃣ LONGEST SUBSTRING WITH MOST K DISTINCT CHARACTERS
# s= aaabbccdd k=2
# similar to above but here k is given

# 1.brute force approach
# create all subarrays, store the distinct element in an arr 
# if the len of arr > k then break
# tc O(n²)   
def longestSubstringKChar(s:str,k:int):
    m=-1
    ll=len(s)
    for i in range(ll):
        noOf=[]
        for j in range(i,ll):
            if s[j] not in noOf:
                if len(noOf)<k:
                    m=max(m,j-i+1)
                    noOf.append(s[j])
                else:
                    break
            else:
                
                m=max(m,j-i+1)
    return m


# 2. optimal one
# similar to 4 optimal one but here k is given
# tc (2n) sc O(k)
def longestSubstringKChar2(arr:str, k:int):
    l=0
    r=0
    no=0
    m=-1
    ll=len(arr)
    no_of=dict()
    while(r<ll):
        if arr[r] in no_of.keys():
            no_of[arr[r]]+=1
        else:
            no_of[arr[r]]=1
            no+=1
        if no>k:
            while((len(no_of.keys())>k)):#doubt why no l<r
                no_of[arr[l]]-=1
                if no_of[arr[l]]==0:
                    no-=1
                    no_of.pop(arr[l])
                    break
                l+=1
            l+=1
        else:
            m=max(m,r-l+1)
        r+=1
    return m


# 3. optimal one more
# tc O(n) sc O(n)
# similar to 4 optimal one more but here k is given
def longestSubstringKChar3(arr:list,k:int):
    l=0
    r=0
    no=0
    m=-1
    ll=len(arr)
    no_of=dict()
    while(r<ll):
        if arr[r] in no_of.keys():
            no_of[arr[r]]+=1
        else:
            no_of[arr[r]]=1
            no+=1
        if no>k:
            if((len(no_of.keys())>k)):#doubt why no l<r
                no_of[arr[l]]-=1
                if no_of[arr[l]]==0:
                    no-=1
                    no_of.pop(arr[l])
                #     break
                # l+=1
            l+=1
        else:
            m=max(m,r-l+1)
        r+=1
    return m



if __name__=="__main__":
    arr=[6,2,3,4,7,2,1,7,1]
    k=4
    # print(maxSumKCards(arr,k))
    s="cadbzabcd"
    # print(longestSubstringWithoutRepeat2(s))
    a=[1,1,1,0,0,0,1,1,1,1,0]
    k=2
    # print(maxConsecutiveOnesIII3(a,k))
    # arr2=[3,3,3,1,2,1,1,2,3,3,4]
    # print(fruitIntoBaskets3(arr2))
    s="aaabbccd"
    print(longestSubstringKChar3(s,3))
    print(longestSubstringKChar2(s,3))
    print(longestSubstringKChar(s,3))
