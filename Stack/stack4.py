# left to check----💀💀💀💀💀✅

# 1️⃣sum of subarrays minimums
# find the sum of the minimum in every subarray
# a=[3,1,2,4] ans=17
# 1 approach
# Tc-O(n)
# find tc of min
def sumOfSubarray(arr:list):
    l=len(arr)
    ans=0
    for i in range(l):
        for j in range(i,l):
            m=min(arr[i:j+1])
            ans+=m
    return ans

# 2 approach
# use pse and nse
# assign index in pse and nse not the element
# instead of -1 assign n
# then ((nse-i)+(i-pse)) is the total no of subarrays in which arr[i] is smallest 
#  multiply it with arr[i] and add to ans
# TC sc O(5n)
def pse(arr:list):
    l=len(arr)
    ans=[]
    stack=[]
    for i in range(l):
        m=-1
        if len(stack)==0:
            stack.append([arr[i],i])
        else:
            while(len(stack)!=0 and stack[-1][0]>arr[i]):
                stack.pop()
            if len(stack)!=0:
                m=stack[-1][1]
            stack.append((arr[i],i))
        ans.append(m)
    return ans

def nse(arr:list):
    a=arr[::]
    arr=arr[::-1]
    l=len(arr)
    ans=[]
    stack=[]
    for i in range(l):
        m=l
        if len(stack)==0:
            stack.append((arr[i],i))
        else:
            while(len(stack)!=0 and stack[-1][1]>=arr[i]):
                stack.pop()
            if len(stack)!=0:
                m=a.index(stack[-1])
            stack.append((arr[i],i))
        ans.append(m)
    return ans[::-1]

def sumOfSubarrays(arr:list):
    l=len(arr)
    ans=0
    pse=pse(arr)
    nse=nse(arr)
    for i in range(l):
        ans+=((i-pse[i])+(nse[i]-i))*arr[i]
    return ans
    

# 2️⃣ sum of subarrays ranges(largest - smallest)
# a=[1 4 3 2] ans 13
# 1 approach
# find the subarray then max(arr)- min(arr)
# tc O(n²)
def sumOfSubarrayRanges(arr:list):
    ans=0
    l=len(arr)
    for i in range(l):
        for j in range(i,l):
            ans+=(max(arr[i:j+1])-min(arr[i:j+1]))
    return ans


# 2 approach
# find the sum of subarray min and max both---left💀💀💀
def pge(arr:list):
    l=len(arr)
    ans=[]
    stack=[]
    for i in range(l):
        m=-1
        if len(stack)==0:
            stack.append((arr[i],i))
        else:
            while(len(stack)!=0 and stack[-1][0]<arr[i]):
                stack.pop()
            if len(stack)!=0:
                m=stack[-1][1]
            stack.append((arr[i],i))
        ans.append(m)
    return ans

def nge(arr:list): 
    l=len(arr)
    ans=[0 for i in range(l)]
    stack=[]
    for i in range(l-1,-1,-1):
        m=l
        if len(stack)==0:
            stack.append((arr[i],i))
        else:
            while(len(stack)!=0 and stack[-1][0]<arr[i]):
                stack.pop()
            if len(stack)!=0:
                m=(stack[-1][1])
            stack.append((arr[i],i))
        ans[i]=m
    return ans

def sumOfSubarrayRanges2(arr:list):
    l=len(arr)
    ans=0
    ans1=0
    p=pge(arr)
    n=nge(arr)
    p1=pse(arr)
    n1=nse(arr)
    for i in range(l):
        ans+=(((i-p[i])+(n[i]-i))*arr[i])
        ans1+=((i-p1[i])+(n1[i]-i))*arr[i]
    return ans-ans1

    
if __name__=="__main__":
    a=[3,1,2,4] 
    # print(sumOfSubarray(a))
    a1=[2,5,1,0,7,9,4]
    # a1=[1,1]
    # print(pge(a1))
    # print(nge(a1))
    a3=[1,4,3,2]
    print(sumOfSubarrayRanges2(a3))
    # print(sumOfSubarrayRanges2(a1))
