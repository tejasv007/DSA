# combinational sum
def combinationalSum1(arr:list,t:int,i:int,s:int,ans:list,n:int,res:list):
    if i>n:
        if s==t:
            res.append(ans)
        return 
    if s<t:
        ans.append(arr[i])
        s+=arr[i]
        combinationalSum1(arr,t,i,s,ans,n,res)
        ans.pop()
    # s-=arr[i]
    combinationalSum1(arr,t,i+1,s,ans,n,res)
    

if __name__=="__main__":
    a=[2,3,6,7]
    res=[]
    (combinationalSum1(a,7,0,0,[],4,res))
    print(res)