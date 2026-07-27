# 1️⃣ Longest Increasing Subsequence ✅checked leetcode
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#nums = [10,9,2,5,3,7,101,18]
# Output: 4
# recursion
# tc 2^N
# sc O(N)(auxillary call stack)
def longestIncreasingSubsequenceHelper(nums,ind,n,prev):
    if ind==n:
        return -1
    len=longestIncreasingSubsequenceHelper(nums,ind+1, n, prev)
    if prev==-1 or nums[ind]>nums[prev]:
        len=max(len,1+ longestIncreasingSubsequenceHelper(nums, ind+1,n, ind))
    return len



def longestIncreasingSubsequence(nums):
    return longestIncreasingSubsequenceHelper(nums,-1,len(nums),-1)


# memoization
# tc O(N*N)
# sc O(N*N)

def longestIncreasingSubsequenceHelperM(nums,ind,n,prev,newarr):
    if ind==n:
        return 0
    if newarr[ind][prev+1]!=-1: return newarr[ind][prev+1]
    len=longestIncreasingSubsequenceHelperM(nums,ind+1, n, prev,newarr)
    if prev==-1 or nums[ind]>nums[prev]:
        len=max(len,1+ longestIncreasingSubsequenceHelperM(nums, ind+1,n, ind,newarr))
    newarr[ind][prev+1]=len
    return len



def longestIncreasingSubsequenceM(nums):
    newarr=[[-1 for j in range(len(nums))] for i in range(len(nums)+1)]
   
    longestIncreasingSubsequenceHelperM(nums,0,len(nums),-1, newarr)
    return newarr[0][0]


# tabulation
# ------------

# 2️⃣ Edit Distance ✅checked leetcode
# # Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# word1 = "horse", word2 = "ros"
# Output: 3
#  tc exponential 3^n
# sc O(n+m)
def editDistanceHelper(i,s1,s2,j):
    if i==-1:return j+1
    if j==-1:return i+1
    if s1[i]==s2[j]:return editDistanceHelper(i-1,s1,s2,j-1)
    a=1+editDistanceHelper(i,s1,s2,j-1)
    b=1+editDistanceHelper(i-1,s1,s2,j)
    c=1+editDistanceHelper(i-1,s1,s2,j-1)
    return min(a,b,c)

def editDistance(s1,s2):
    return editDistanceHelper(len(s1)-1,s1,s2,len(s2)-1)



# memoization
# sc O(2(n+m))
# tc O(n*m)

def editDistanceHelperM(i,s1,s2,j,newarr):
    if i==-1:return j+1
    if j==-1:return i+1
    if newarr[i][j]!=-1:
        return newarr[i][j]
    if s1[i]==s2[j]:return editDistanceHelperM(i-1,s1,s2,j-1,newarr)
    a=1+editDistanceHelperM(i,s1,s2,j-1,newarr)
    b=1+editDistanceHelperM(i-1,s1,s2,j,newarr)
    c=1+editDistanceHelperM(i-1,s1,s2,j-1,newarr)
    newarr[i][j]=min(a,min(b,c))
    return newarr[i][j]



def editDistanceM(s1,s2):
    newarr=[[-1 for i in range(len(s2))] for j in range(len(s1))]
    return editDistanceHelperM(len(s1)-1,s1,s2,len(s2)-1,newarr)
    # return newarr


# 3️⃣ Longest Palindromic Subsequence
# here we build one more string which is reverse of the given string
# then use longest common subsequence but return a string
# "abbcccba"-------- stucking over here
# def longestCommonSequencesHelperM(ind1,ind2,s1,s2,newArr,s):
#     if ind1<0 or ind2 <0:
#         return s 
#     if newArr[ind1][ind2]!=-1:return newArr[ind1][ind2]
#     if s1[ind1]==s2[ind2]:
#         newArr[ind1][ind2]=longestCommonSequencesHelperM(ind1-1,ind2-1,s1,s2,newArr,s)+s1[ind1]
#         return newArr[ind1][ind2]
#     l=longestCommonSequencesHelperM(ind1-1,ind2,s1,s2,newArr,s)
#     r=longestCommonSequencesHelperM(ind1,ind2-1,s1,s2,newArr,s)
#     if len(l)>=len(r):
#         newArr[ind1][ind2]= l
#     else:
#         newArr[ind1][ind2]= r
#     # newArr[ind1][ind2]=max(len(longestCommonSequencesHelperM(ind1-1,ind2,s1,s2,newArr)),longestCommonSequencesHelperM(ind1,ind2-1,s1,s2,newArr))
#     return newArr[ind1][ind2]


# def longestCommonSequencesM(s1,s2):
#     newArr=[[-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
#     s=""
    
#     return longestCommonSequencesHelperM(len(s1)-1,len(s2)-1,s1,s2,newArr,s)


# def longestPalimdromicSubsequenceM(s1):
#     return longestCommonSequencesM(s1,s1[::-1])

def lll(s1,f,l):
    if f>l:
        return ""
    if f==l:
        return s1[f]
    if s1[f]==s1[l]:
        return s1[f]+lll(s1,f+1,l-1)+s1[f]
    m=(lll(s1,f+1,l))
    n=(lll(s1,f,l-1))
    if len(m)<=len(n):
        return n
    return m
    
def lllm(s1,f,l,dp):
    if f>l:
        return ""
    if f==l:
        return s1[f]
    if dp[f][l]!=-1:
        return dp[f][l]
    if s1[f]==s1[l]:
        dp[f][l]=s1[f]+lllm(s1,f+1,l-1,dp)+s1[f]
        return dp[f][l]
    m=(lllm(s1,f+1,l,dp))
    n=(lllm(s1,f,l-1,dp))
    if len(m)<=len(n):
        dp[f][l]=n
        return n
    dp[f][l]=m
    return m

# 4️⃣ Wildcard Matching
# 
def wildCardMatchingHelper(j,i,s1,s2):
    if j<0 and i<0:
        return True
    if j>0 and i<0:
        return False
    if j<0 and i>0:
        for _ in range(i):
            if s1[_]!="*":
                return False
        return True
    if s1[i]==s2[j] or s1[i]=="?":
        return wildCardMatchingHelper(j-1,i-1,s1,s2)
    if s1[i]=="*":
        return wildCardMatchingHelper(j-1,i,s1,s2) or wildCardMatchingHelper(j,i-1,s1,s2)
    return False

def wildCardMatching(s1,s2):
    return wildCardMatchingHelper(len(s2)-1,len(s1)-1,s1,s2)


# Memoization
def wildCardMatchingHelperM(j,i,s1,s2,newarr):
    if j<0 and i<0:
        return True
    if j>=0 and i<0:
        return False
    if j<0 and i>=0:
        for _ in range(i):
            if s1[_]!="*":
                return False
        return True
    if newarr[i][j]!=-1:
        return newarr[i][j]
    if s1[i]==s2[j] or s1[i]=="?":
        newarr[i][j]=wildCardMatchingHelperM(j-1,i-1,s1,s2,newarr)
        return newarr[i][j]
    elif s1[i]=="*":
        newarr[i][j]=wildCardMatchingHelperM(j-1,i,s1,s2,newarr) & wildCardMatchingHelperM(j,i-1,s1,s2,newarr)
        return newarr[i][j]
    
    newarr[i][j]=False
    return newarr[i][j]

def wildCardMatchingM(s1,s2):
    newarr=[[-1 for i in range(len(s2))] for j in range(len(s1))]
    return wildCardMatchingHelperM(len(s2)-1,len(s1)-1,s1,s2,newarr)
    # return newarr


if __name__=="__main__":
    nums =  [10,9,2,5,3,7,101,18]
    # nums=[4,10,4,3,8,9]
    # print(longestIncreasingSubsequenceM(nums))
    word1 ="intention"
    word2 = "execution"
    # print(editDistanceM(word1,word2))
    s1="*"
    s2="aa"
    # print(wildCardMatchingM(s1,s2))
    s1="bbcacbab"
    s1="abbcccba"
    # print(longestPalimdromicSubsequenceM(s1))
    dp=[[-1 for i in range(len(s1)+1)] for j in range((len(s1)))]
    print(lllm(s1,0,len(s1)-1,dp))