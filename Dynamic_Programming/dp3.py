# ⭐⭐⭐⭐⭐⭐⭐
# ⭐⭐⭐📝📖 DP on Subsequences/Subsets problems
# Subsequences--> contigious or non contigious part of array and follow that order
# subarray --> contigious oart of array and follow the order

# 1️⃣ subset sum equal to k --gfg ✅ checked
# Given an array of positive integers arr[] and a value sum, determine if there is a subset of arr[] with sum equal to given sum. 
# not use a no more than the count present in array
# here we use concept of pick and not pick
# we use ind and target, ind tell us that at which index we are in and target tell us which is our target
# base case if i >n then ret false
# if target> arr[i] then pick else return false
# at last return or of pick and nonpick
# tc O(2*len(Arr))
# sc O(len(arr)(call stack))
# arr=[3, 34, 4, 12, 5, 2]; sum = 9
# ans = true 
def subsetSumEqualKHelper(ind:int,target:int,arr):
    if target==0:return True
    if ind ==len(arr):return False
    nonpick=subsetSumEqualKHelper(ind+1,target,arr)
    pick=False
    if target>=arr[ind]:
        pick=subsetSumEqualKHelper(ind+1,target-arr[ind],arr)
    print(pick or nonpick)
    return pick or nonpick

def subsetSumEqualK(arr,target):
    return subsetSumEqualKHelper(0,target,arr)


# memoization
# we build 2 d matrix of row consist of len(Arr) and column consist of target len
# tc O(len(Arr))
# sc O(len(Arr)*target+len(arr)(call stack))
def subsetSumEqualKHelperM(ind:int,target:int,arr,newArr):
    if target==0:return True
    if ind ==len(arr):return False
    if newArr[ind][target]!=-1:return newArr[ind][target]
    nonpick=subsetSumEqualKHelperM(ind+1,target,arr,newArr)
    pick=False
    if target>=arr[ind]:
        pick=subsetSumEqualKHelperM(ind+1,target-arr[ind],arr,newArr)
    newArr[ind][target]=pick or nonpick
    return pick or nonpick


def subsetSumEqualKM(arr,target):
    newArr=[[-1 for i in range(target+1)] for j in range(len(arr)) ]
    return subsetSumEqualKHelperM(0,target,arr,newArr)

# tabulation left----------


# 2️⃣ 0/1 knapsack problem---✅checked in gfg
# Given two arrays, val[] and wt[], where each element represents the value and weight of an item respectively, and an integer W representing the maximum capacity of the knapsack (the total weight it can hold).

# The task is to put the items into the knapsack such that the total value obtained is maximum without exceeding the capacity W.

# Note: You can either include an item completely or exclude it entirely — fractional selection of items is not allowed. Each item is available only once.

# W = 4, val[] = [1, 2, 3], wt[] = [4, 5, 1]
# ans 3
# here we have to find subsequence of wt array
# use pick and not pick var to take or not take wts,
# one change is that if target <wt[any index] then pick is 0 as we are not taking it else we take it
def knapsack01Helper(ind:int, target,wt:list, val:list):
    if target==0:
        return 0
    if ind==len(wt)-1:return 0
    nonpick=0+knapsack01Helper(ind+1,target,wt,val)
    pick=0
    if target>=wt[ind]:
        pick=val[ind]+knapsack01Helper(ind+1,target-wt[ind],wt,val)
    print(pick,nonpick)
    return max(pick,nonpick)

def knapsack01(wt,val,w):
    return knapsack01Helper(-1,w,wt,val)

# memoization
# here we use 2d array-->why--> becoz we have to keep in mind the target also
def knapsack01HelperM(ind:int, target,wt:list, val:list,newArr):
    if target==0:
        return 0
    if ind==len(wt)-1:return 0
    if newArr[ind][target]!=-1:return newArr[ind][target]
    nonpick=0+knapsack01HelperM(ind+1,target,wt,val,newArr)
    pick=0
    if target>=wt[ind]:
        pick=val[ind]+knapsack01HelperM(ind+1,target-wt[ind],wt,val,newArr)
    newArr[ind][target]=max(pick,nonpick)
    return max(pick,nonpick)

def knapsack01M(wt,val,w):
    newArr=[[-1 for i in range(w+1)] for j in range(len(wt))]
    return knapsack01HelperM(-1,w,wt,val,newArr)


# tabulation
# tc O()
def knapsack01HelperT(target,wt:list, val:list):
    newArr=[[0 for i in range(target+1)] for j in range(len(wt))]
    for i in range(wt[0],target+1):
        newArr[0][i]=val[0]
    for i in range(1,len(wt)):
        for j in range(target+1):
            np=newArr[i-1][j]
            p=-1
            if wt[i]<=j:
                p=val[i]+newArr[i-1][j-wt[i]]
            newArr[i][j]=max(np,p)
    return newArr[-1][-1]

# 3️⃣Coin change---checked✅ in leetcode
# 💀 tc and sc ------left
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

#  coins = [1,2,5], amount = 11
# output 3


# recursion
# tc O(2**(amt+ind))--check it
def coinChangeHelper(coins,amt,ind,amount):
    if amt==amount:
        return 0
    if amt>amount:
        return 10**8
    if ind<0:
        return 10**8
    l=1+coinChangeHelper(coins,amt+coins[ind],ind,amount)
    r=coinChangeHelper(coins,amt,ind-1,amount)
    return min(l,r)


def coinChange(coins,amount):
    a= coinChangeHelper(coins,0,len(coins)-1,amount)
    if a>=10**8:
        return -1
    return a 



# memoization
def coinChangeHelperM(coins, amt, ind, amount, newArr):
    if amt==amount:
        return 0
    if amt>amount:
        return 10**8
    if ind<0:
        return 10**8
    if newArr[ind][amt]!=-1:return newArr[ind][amt]
    l=1+coinChangeHelperM(coins,amt+coins[ind],ind,amount,newArr)
    r=coinChangeHelperM(coins,amt,ind-1,amount,newArr)
    newArr[ind][amt]=min(l,r)
    return newArr[ind][amt]
    
def coinChangeM(coins,amount):
    newArr=[[-1 for i in range(amount+1)] for j in range(len(coins))]
    coinChangeHelperM(coins,0,len(coins)-1,amount,newArr)
    if newArr[len(coins)-1][0]>=10**8:return -1
    if newArr[len(coins)-1][0]==-1:return 0
    return newArr[len(coins)-1][0]
        
# tabulation--Left


#4️⃣  Longest common sequences------✅checked in leetcode
# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
#  text1 = "abcde", text2 = "ace" 
# Output: 3  

# recursion
# here we keep two pointers that is ind1 and ind2 
# one for one string and other for other string
# now if str1 at ind1 == str2 at ind2 then return 1 +fn(ind1-1, ind2-1)
# else run two fn and take max of both ie
# return max(fn(ind1-1,ind2),fn(ind1,ind2-1))
# tc O(2^(n+m))
# sc O(n*m)
def longestCommonSequencesHelper(ind1,ind2,s1,s2):
    if ind1<0 or ind2 <0:
        return 0
    if s1[ind1]==s2[ind2]:
        return 1+longestCommonSequencesHelper(ind1-1,ind2-1,s1,s2)
    return max(longestCommonSequencesHelper(ind1-1,ind2,s1,s2),longestCommonSequencesHelper(ind1,ind2-1,s1,s2))

def longestCommonSequences(s1,s2):
    return longestCommonSequencesHelper(len(s1)-1,len(s2)-1,s1,s2)

# memoization
# same as recursion but take a 2d list which store values acc to indexies
# tc O(n*m)
# sc O(m*n)+ O(n+m)(auxillary)
def longestCommonSequencesHelperM(ind1,ind2,s1,s2,newArr):
    if ind1<0 or ind2 <0:
        return 0
    if newArr[ind1][ind2]!=-1:return newArr[ind1][ind2]
    if s1[ind1]==s2[ind2]:
        newArr[ind1][ind2]=1+longestCommonSequencesHelperM(ind1-1,ind2-1,s1,s2,newArr)
        return newArr[ind1][ind2]
    newArr[ind1][ind2]=max(longestCommonSequencesHelperM(ind1-1,ind2,s1,s2,newArr),longestCommonSequencesHelperM(ind1,ind2-1,s1,s2,newArr))
    return newArr[ind1][ind2]

def longestCommonSequencesM(s1,s2):
    newArr=[[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    return longestCommonSequencesHelperM(len(s1)-1,len(s2)-1,s1,s2,newArr)

# tabulation--Left


# 5️⃣Coin Change II----✅checked
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

# You may assume that you have an infinite number of each kind of coin.

# The answer is guaranteed to fit into a signed 32-bit integer.

# recursion
# here we count the ways and add up
# 💀 tc and sc ------left

def coinChangeIIHelper(coins,amt,ind,amount):
    if amt==amount:
        return 1
    if amt>amount:
        return 0
    if ind<0:
        return 0
    l=coinChangeIIHelper(coins,amt+coins[ind],ind,amount)
    r=coinChangeIIHelper(coins,amt,ind-1,amount)
    return l+r


def coinChangeII(coins,amount):
    return coinChangeIIHelper(coins,0,len(coins)-1,amount)
    

# memoization
def coinChangeIIHelperM(coins, amt, ind, amount, newArr):
    if amt==amount:
        
        return 1
    if amt>amount:
        return 0
    if ind<0:
        return 0
    if newArr[ind][amt]!=-1:
        return newArr[ind][amt]
    l=coinChangeIIHelperM(coins,amt+coins[ind],ind,amount,newArr)
    r=coinChangeIIHelperM(coins,amt,ind-1,amount,newArr)
    newArr[ind][amt]=l+r
    return newArr[ind][amt]
    
def coinChangeIIM(coins,amount):
    newArr=[[-1 for i in range(amount+1)] for j in range(len(coins))]
    return coinChangeIIHelperM(coins,0,len(coins)-1,amount,newArr)
    
    
# tabulation--Left


if __name__=="__main__":


    # arr=[3, 34, 4, 12, 5, 2]; sum = 9
    # print(subsetSumEqualKHelperM(0,sum,arr,newArr))
    # print(subsetSumEqualKM(arr,sum))
    # W = 4; val = [1, 2, 3]; wt = [4, 5, 1]
    W = 5; val = [10, 40, 30, 50]; wt = [5, 4, 2, 3] 
    # W = 3; val = [1, 2, 3]; wt = [4, 5, 6] 
    # print(knapsack01M(wt,val,W))
    # print(knapsack01HelperT(W,wt,val))
    # print(fn(5,"a?b?a"))
    t1 = "abcde";t2 = "ace" 
    # print(longestCommonSequencesM(t1,t2))
    amount = 500;coins = [1,2,5]
    # print(coinChangeHelper(coins,0,len(coins)-1,amount))
    print(coinChangeII(coins,amount))
    print(coinChangeIIM(coins,amount))
    