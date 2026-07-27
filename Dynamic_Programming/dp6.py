# 1️⃣ Matrix Chain Multiplication checked ✅ in gfg
# Difficulty: HardAccuracy: 49.64%Submissions: 193K+Points: 8
# Given an array arr[] which represents the dimensions of a sequence of matrices where the ith matrix has the dimensions (arr[i-1] x arr[i]) for i>=1, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.
# Input: arr[] = [2, 1, 3, 4]
# Output: 20
# Explanation: There are 3 matrices of dimensions 2 × 1, 1 × 3, and 3 × 4, Let this 3 input matrices be M1, M2, and M3. There are two ways to multiply: ((M1 x M2) x M3) and (M1 x (M2 x M3)), note that the result of (M1 x M2) is a 2 x 3 matrix and result of (M2 x M3) is a 1 x 4 matrix. 
# ((M1 x M2) x M3)  requires (2 x 1 x 3) + (2 x 3 x 4) = 30 
# (M1 x (M2 x M3))  requires (1 x 3 x 4) + (2 x 1 x 4) = 20. 
# The minimum of these two is 20.


# recursion---
def matrixChainMultiplication(i,j,arr):
    if i==j:return 0
    mini=2**30
    for k in range(i,j):
        steps=arr[i-1]*arr[k]*arr[j]+matrixChainMultiplication(i,k,arr)+matrixChainMultiplication(k+1,j,arr)
        mini=min(mini,steps)
    return mini
# memoization is left----'⚡💀💀

# tabulation---
def matrixChainMultiplicationT(arr):
    new=[[-1 for i in range(len(arr))] for k in range(len(arr))]
    for i in range(len(arr)):
        new[i][i]=0
    for i in range(len(arr)-1,0,-1):
        for j in range(i+1,len(arr)):
            mini=2**30
            steps=0
            for k in range(i,j):
                steps=arr[i-1]*arr[k]*arr[j]+new[i][k]+new[k+1][j]
                if steps<mini:
                    mini=steps
            new[i][j]=mini
    return new[1][len(arr)-1]
if __name__=="__main__":
    # arr1=[200, 200, 200, 199, 200, 200 ,200 ,200, 200 ,200 ,200 ,200 ,200, 200, 200 ,200, 200, 200 ,200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200 ,200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
    # arr= [2, 1, 3, 4]
    arr1= [1, 2, 3, 4, 3]
    
    # print(matrixChainMultiplication(1,len(arr)-1,arr))
    print(matrixChainMultiplicationT(arr1))
    