# left to check----💀💀💀💀💀✅

# 1️⃣Min stack
# minimum element in the stack
# 1 brute force
# Tc-O(n)
# traverse whole array and provide min no exist--(can diff in python(check💀))
class MinStack1:
    def __init__(self):
        self.s=[]
    def push(self,x:int):
        self.s.append(x)

    def pop(self):
        if len(self.s)==0:
            return "empty"
        return self.s.pop()
    def getMin(self):
        return min(self.s)
    
# 2. better
# use hashmap store current and min one
# tc-O(1) sc-O(2n)
class MinStack2:
    def __init__(self):
        self.s=[]
        self.m=1234567
    def push(self,x:int):
        self.m=min(self.m,x)
        self.s.append([x,self.m])

    def pop(self):
        if len(self.s)==0:
            return "empty"
        return self.s.pop()
    def getMin(self):
        if len(self.s)==0:return "empty"
        return self.s[-1][1]
    
# 3. optimal---- working well ---need to confirm✅✅
# use a var which store the min
# but if pop out the min then var would be change
# so use 2 *val-prevmin=new val( val is the min no, prevminn is the prev min no and new val store in stack instead of ele)
# when ele <new val then it mean new val is the element
# and if min pop out assign new val to prev min but formula 
# Sc-O(n) Tc-O(1)
class MinStack3:
    def __init__(self):
        self.s=[]
        self.mini=123456789
    def push(self,x:int):
        if len(self.s)==0:
            self.s.append(x)
            self.mini=x
        else:
            if self.mini>x:
                self.s.append((2*x)-self.mini)
                self.mini=x
            else:
                self.s.append(x)
    def pop(self):
        if len(self.s)==0:
            return "empty"
        if self.s[-1]<self.mini:
        
            self.mini=((2*self.mini)-self.s[-1])
            return self.s.pop()
        return self.s.pop()
    
    def getMin(self):
        if len(self.s)==0:
            return "empty"
        if self.s[-1]<self.mini:
            return self.mini
        return self.mini


    def top(self):
        if len(self.s)==0:
            return "empty"
        if self.s[-1]<self.mini:
            return self.mini
        return self.s[-1]

    

# 2️⃣ Next Greatest Element(monotonic stack(stack follow a specific order))
# 6 0 8 1 3
# 8 8 -1 3 -1
# 1. brute force 
# traverse from next element to end and then find the greatest one
# find max tc 
# TC O(n²) SC O(n)
def NGE1(arr:list):
    ans=[]
    for i in range(len(arr)-1):
        if max(arr[i+1:]) <arr[i]:
            ans.append(-1)
        else:
            ans.append(max(arr[i+1:]))
    ans.append(-1)
    return ans

# 2 optimal
# use stack 
# start from end push element from arr to stack 
# when curr ele < top ele push the curr and append top ele in ans
# if not then pop out elements from the stack till stack get empty or the top ele> curr ele, if stack get empty append -1 otherwise top ele
# tc and sc O(2n)
def NGE2(arr:list):
    stack=[]
    ans=[0 for i in range(len(arr))]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            ans[i]=-1
            stack.append(arr[i])
        else:
            while(len(stack)!=0 and stack[-1]<=arr[i]):
                stack.pop()
            if len(stack)==0:
                ans[i]=-1
                stack.append(arr[i])
            else: ans[i]=(stack[-1])
            stack.append(arr[i])
    return ans

# 3️⃣NGE 2
# its is ame as nge but here if dont find in right then start from the start like in circular queue
# 2 10 12 1 11
# 10 12 -1 11 12
# 1 brute force approach
# iterate from whole array and also in each iterate from i+1 to i+n-1
# Tc O(N²) Sc O(N)
def NGE2_1(arr:list):
    l=len(arr)
    ans=[0 for i in range(l)]
    for i in range(l):
        m=-1
        for j in range(i+1,i+l-1):
            if arr[j%l]>arr[i]:
                m=arr[j%l]
                break
        ans[i]=m
    return ans
        
        

# 2 optimal approach
# TC O(4n) Sc O(2n)
# follow the nge1 optimal method but here make array two times 
# increase the no to 2n
# then follow the approach when the no get equal to len-1 then the real one array start so then start changing the ans array 
def NGE2_2(arr:list):
    stack=[]
    l=len(arr)
    ans=[0 for i in range(l)]
    for i in range((2*l)-1,-1,-1):
        m=-1
        if len(stack)==0:
            stack.append(arr[i%l])
        else:
            while(len(stack)!=0 and stack[-1]<=arr[i%l]):
                stack.pop()
            if len(stack)!=0:
                m=stack[-1]
            stack.append(arr[i%l])
        if i<l:
            if m==arr[i]:
                ans[i]=-1
            else: ans[i]=m
           
    return ans
            

# 4️⃣Previous smallest element
# find the smallest element exist before the curr element
# 4 5 2 1 8
# -1 4 -1 -1 1
# 1 brute force approach
# iterate the arr and in each, iterate the arr one more time from i-1 to 0  
# if find no < the curr one break and assign it to ans arr
# tc O(n²) sc- O(n)
def pse1(arr:list):
    l=len(arr)
    ans=[0 for i in range(l)]
    ans[0]=-1
    for i in range(1,l):
        m=-1
        for j in range(i-1,-1,-1):
            if arr[j]<arr[i]:
                m=arr[j]
                break
        ans[i]=m
    return ans

# 2 optimal approach
# use the stack to store the element
# if stack is not empty pop out all element from stack which is greater then the append the element
# tc O(2n) sc O(2n)
def pse2(arr:list):
    l=len(arr)
    ans=[0 for i in range(l)]
    stack=[]
    for i in range(len(arr)):
        m=-1
        if len(stack)==0:
            stack.append(arr[i])
        else:
            while(len(stack)!=0 and stack[-1]>=arr[i]):
                stack.pop()
            if len(stack)!=0:
                m=stack[-1]
                stack.append(arr[i])
            
        ans[i]=m
    return ans



# 5️⃣trapping rainwater
# 1 approach
# build array of nge and pse
# if nge(reverse) or nge -1 then leave it
# else add min(pse,nge)-arr[i]  to ans
# Tc O(3n) sc O(2n)
def trappingRainwater(arr:list):
    nge=NGE2(arr)
    nge2=NGE2(arr[::-1])[::-1]
    print(nge)
    print(nge2)
    ans=0
    l=len(arr)
    for i in range(l):
        if nge[i]!=-1 and nge2[i]!=-1:
            ans= ans+ (min(nge2[i],nge[i])-arr[i])
    return ans

# 2 approach--two pointer approach--- not done---- not understand-- need 100% concentration💀💀💀💀

if __name__=="__main__":
    # obj=MinStack3()
    # obj.push(3)
    # obj.push(8)
    # obj.push(2)
    # obj.push(1)
    # obj.push(0)

    # print(obj.getMin())#0
    # (obj.pop())
    # (obj.pop())

    # # print(obj.mini)
    # print(obj.getMin())#2
    # (obj.pop())
    # print(obj.getMin())#3
    # (obj.pop())
    # print(obj.getMin())#3
    # a=[6 ,0 ,8 ,1 ,3]
    # print(NGE2(a))
    a1=[2,10,12,1,11]
    # print(NGE2_1(a1))
    # print(NGE2_2(a1))
    a2=[4 ,5 ,2 ,1 ,8]
    # print(pse2(a1))
    # print(pse2(a2))
    tr=[1,0,2,1,0,1,3,2,1,2,1]
    print(trappingRainwater(tr))
    # print(NGE2(tr))
    