# 1️⃣Valid Parenthesis String
# opening parenthesis should have a closing parenthesis
# opening parenthesis should lie before closing parenthesis 
# asterisk * can be replace with (,) or nothing
# tell string is valid parenthesis or not
# (), (*), (*)) ->true
# )(), (**(-> false
# ()*)*()
# brute force
# here we build a var count, if we get ( count+=1 and if get ) count-=1 and if get * run the recursion and replace * by ( then ) and then ""
# tc-O(3^n) sc-O(n)(n len of s)
def validParenthesisString(s:str,i=0,c=0):
    if c<0:
        return False
    if i==len(s):
        if c==0:return True
        return False
    if s[i]=="(": return validParenthesisString(s,i+1,c+1)
    if s[i]==")": return validParenthesisString(s,i+1,c-1)
    a=validParenthesisString(s,i+1,c+1)
    b=validParenthesisString(s,i+1,c-1)
    c=validParenthesisString(s,i+1,c)
    if a==True or b==True or c==True:return True
    return False


# solve by dp----💀💀💀💀💀⚡⚡⚡⚡⚡⚡
# optimal---confuse --checked correct
# here we use two var min and max , if we encounter * we add 0 to min and +1 to max 
# if encounter ( min and max +1 and ) min and max -1
# tc O(n) sc O(1)
def validParenthesisStringII(s:str):
    mMin=0
    mMax=0
    for i in s:
        if i=="(":
            mMin+=1
            mMax+=1
        elif i==")":
            mMax-=1;mMin-=1  
        else:
            mMin-=1
            mMax+=1
        if mMin<0:mMin=0
        if mMax<0:return False
    print(mMin,mMax)
    if mMin==0:return True
    return False
    

# 2️⃣Candy
# each children have at least one candy
# children with higher rating has candy > neighbour candies
# provide an array with rating
# find the minimum candies which can satisfy above two conditions 
# arr=[1,2,3] candies=6 ie 1+2+3
# arr=[1,3,2,1] candies=7 ie 1+3+2+1
# here firstly we assign cookies according to left side--> that is if rating is > the prev one assign prev one+1 candies else if rating<the prev one assign 1 candies
# secondly assign cookies according to right side--> start from last, if the next rating< current one then next candies +1 else if next rating>current assign 1
# then ans be the max of left[i] and right[i]
# eg arr=[1,2,4,3,2,1,1,3,5,6,4,0,0]
# left side==> 1 2 3 1 1 1 1 2 3 4 1 1 1
# right side==> 1 1 4 3 2 1 1 1 1 3 2 1 1
# ans=[1,2,4,3,2,1,1,2,3,4,2,1,1]
# tc O(3n) sc O(2n)
# checked correct
def candy(arr:list):
    l=len(arr)
    left=[0 for i in range(l)]
    right=[0 for i in range(l)]
    left[0]=1
    for i in range(1,l):
        if arr[i]>arr[i-1]:left[i]=left[i-1]+1
        else:
            left[i]=1
    right[-1]=1
    for i in range(l-2,-1,-1):
        if arr[i]>arr[i+1]:right[i]=right[i+1]+1
        else:
            right[i]=1

    count=0
    for i in range(l):
        count+=(max(left[i],right[i]))
    return count
# optimal tc O(2n) sc O(n)
# not use right array just find the max add add up
def candyI(arr:list):
    l=len(arr)
    left=[0 for i in range(l)]
    right=[0 for i in range(l)]
    left[0]=1
    for i in range(1,l):
        if arr[i]>arr[i-1]:left[i]=left[i-1]+1
        else:
            left[i]=1
    prev=1
    count=max(1,left[-1])

    for i in range(l-2,-1,-1):
        if arr[i]>arr[i+1]:
            prev=prev+1
            
        else:
            prev=1
        count+=(max(left[i],prev))

    # for i in range(l):
    #     count+=(max(left[i],right[i]))
    return count

# most optimal approach
# if dont know previous dont get it in interviews
# concept --slope
# build two var--> peak and down
# peak store the max from the / and down store the max from \ 
# if peak > down then sum=sum-down+peak
#----💀💀💀💀💀⚡⚡⚡⚡⚡⚡ -----



# 3️⃣ Fractional Knapsack Algorithm
# given n values and every value have price and weight to it and max weight which we can carry
# we can take fractional weight also
# find out the maximum cost 
# arr=[(200,50),(100,50),(60,10),(100,20)]
# w=90
# ans=380
# in this we build a new 2d array which store the unit weight cost and sort it according to unit weight asc to desc
# then add the cost and subtract the weight according to taken weight by it then if the weight get < the weight of article then-->
# n=article weight/weight (remaining)
# cost+=(article cost/n)
# tc O(2n+nlogn) sc-O(3n)
def fractionalKnapsack(arr:list,w:int):
    d=[]
    for i in arr:
        new=[]
        new.append(i[0]/i[1])
        new.append(i[0])
        new.append(i[1])
        d.append(new)
    newd=sorted(d,key=lambda i:i[0],reverse=True)
    cost=0
    i=0
    while(i<len(arr) ):
        if w>=newd[i][2]:
            w-=newd[i][2]
            cost+=newd[i][1]
        else:
            n=newd[i][2]/w
            cost+=(newd[i][1]/n)
            break
        i+=1
    return cost


# ----------------------------COMPLETED GREEDY(SOME ARE LEFT---(EITHER THEY ARE OUT OF MY UNDERSTANDING OR NEED ANOTHER DATA STRUCTURE OR ALGORITHM WHICH I HAVENT LEARNT YET))
if __name__=="__main__":

    s="()*)*("
    # s="(*()*)*("
    s="()*()*()*"
    s="(()*"
    s="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
    # print(validParenthesisString(s))
    # print(validParenthesisStringII(s))
    # arr=[1,2,4,3,2,1,1,3,5,6,4,0,0]
    arr=[(200,50),(100,50),(60,10),(100,20)]
    # a=sorted(arr,key=lambda i:i[1])
    # print(a)
    print(fractionalKnapsack(arr,90))
    # print(candy(arr))
    # print(candyI(arr))
