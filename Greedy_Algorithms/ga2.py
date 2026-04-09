# 1️⃣Job Sequencing Problem 
# given n no of jobs everyone has id, deadline, and profit
# on single day can perform a single job
# dealine should not be cross
# we can complete the job before or till deadline but not after it
# find the max profit 
#id  deadline  profit
# 1     4       40
# 2     1       10
# 3     1       40
# 4     1       30
# ans 80 as on day 1 we perform id 3 job then on day 2 we perform id 1 job

# id=[6,3,4,2,5,8,1,7]
# deadline1=[2,6,6,5,4,2,4,2]
# profit1=[80,70,65,60,25,22,20,10]
# ans=342
# here we first sort the profit asc to desc
# then build an array of max days (here we build array of 4)
# traverse the deadline if array at deadline is empty then make assign the array with the job id, if exist then decrease the index if find empty assign the job id and add on the profit
# tc O(n+n+max deadline) sc O(3n +max deadline)(dict space💀💀💀💀 find)


def jobScheduingProblem(job:list,deadline:list,profit:list):
    d=dict()#O(3N)
    for i in range(len(profit)):#O(N)
        d[profit[i]]=[deadline[i],job[i]]
    arr=[-1 for j in range(len(job))]#O(maxdeadline)
    profit.sort(reverse=True)
    countProfit=0
    count=0
    for i in profit:#O(N)
        a=d[i]
        if arr[a[0]] ==-1:
            arr[a[0]]=a[1]
            countProfit+=i
            count+=1
        else:
            j=a[0]
            while(j>-1):#O(max deadline)
                if arr[j]==-1:
                    countProfit+=i
                    arr[j]=a[1]
                    count+=1
                    break
                j-=1
    return countProfit,  count


# 2️⃣ N Meeting in One Room
# start=[0,3,1,5,5,8]
# end=[5,4,2,9,7,9]
# ans= 4-->(1,2)(3,4)(5,7)(8,9)
# order=[3,2,5,6]
# start indicate the starting time of meet and end indicate the ending time of meet
# find the max no of meet and the order of meeting that can be held in one room
# build a dict which contain end start and order
# sort the end, build a freetime var and arr which store the order
# then check if the start >freetime if yes then update freetime =end
# tc O(2n+nlogn) sc O(4n)

def nMeetingOneRoom(start:list,end:list):
    d=dict()
    for i in range(len(start)):
        if end[i] in d.keys():
            a=d[end[i]]
            if a[0]<start[i]:
                a[0]=start[i]
        else:
            d[end[i]] =[start[i],i+1]
            
    end.sort()
    freeTime=end[0]
    o=d[end[0]]
    order=[o[1]]
    for i in range(1,len(end)):
        d1=d[end[i]]
        if d1[0] > freeTime:
            freeTime=end[i]
            order.append(d1[1])
    return len(order), order

# 3️⃣ Non Overlapping Intervals
# intervals=[(1,2)(2,3)(3,4)(1,3)] ans 1
# intervals=[(0,5),(3,4),(1,2),(5,9),(5,7),(7,9)] ans 2
# here we see 1,2 and 2,3 are overlapping with 1,3
# find the min intervals which can be remove so that there will be no more overlapping
# it is similar to n meetings in one room
# tc O(2n+nlogn) sc O(4n)
# we can do it without using dict also

def nonOverlappingIntervals(intervals:list):
    d=dict()
    end=[]
    k=0
    for j in intervals:
        if j[1] in d.keys():
            a=d[j[1]]
            if a[0]<j[0]:
                a[0]=j[0]
        else:
            d[j[1]]=[j[0],k+1]
            end.append(j[1])
        k+=1
    end.sort()
    o=d[end[0]]
    order=[o[1]]
    freeTime=end[0]
    for i in range(1,len(end)):
        new=d[end[i]]
        if freeTime<=new[0]:
            freeTime=end[i]
            order.append(new[1])
    return len(intervals)-len(order)


# 4️⃣Insert Intervals 
# intervals=[[1,3],[6,9]]
# newintervals=[2,5]
# ans=[[1,5][6,9]]
# intervals=[[1,3],[6,9]]
# newintervals=[4,5]
# ans=[[1,3],[4,5],[6,9]]
# intervals=[[1,2],[3,4],[6,7],[8,10],[12,16]]
# newintervals=[5,8]
# ans=[[1,2],[3,4],[5,10],[12,16]]

# here intervals are not overlapping and are in sorted order now task is to insert the new intervals in the intervals so that there is no overlapping   
# return the updated intervals array
# tc O(n)
def insertIntervals(intervals:list,newIntervals:list):
    a=newIntervals[0]
    b=newIntervals[1]
    for i in range(len(intervals)):
        if a<intervals[i][0]:
            break
        else:
            if a<intervals[i][1]:
                a=intervals[i][0]
                intervals.remove(intervals[i])
                break
    j=i
    while(j<len(intervals)):
        if b<intervals[j][0]:
            break
        else:
            if b<intervals[j][1]:
                b=intervals[j][1]
                intervals.remove(intervals[j])
                break
        intervals.remove(intervals[j])
    intervals.insert(i,[a,b])
    return intervals
        



# 5️⃣Minimum number of platforms required in a railway station
# arr=[900,945,955,1100,1500,1800]
# dep=[920,1200,1130,1150,1900,2000]
# ans 3
# given arrive time and departure time of train
# find the Minimum number of platforms required in a railway station so that all train arrive and depart

# here we find the overlapping train timing using a var name maxC which store the max c
# not complete
# left if (statements)💀💀💀💀💀💀💀💀💀
# tc O(n²)
def minNoPlatformRailway(arr:list,dep:list):
    maxC=0
    for i in range(len(arr)):
        c=0
        for j in range(i+1,len(arr)):
            if (arr[j]>arr[i] and arr[j]>dep[i]) or (arr[j]>arr[i] and arr[j]<dep[i]) or (arr[j]<arr[i] and arr[j]<dep[i]) or (arr[j]<arr[i] and arr[j]<dep[i]):
                c+=1
        print(c)
        maxC=max(maxC,c)
    return maxC

# OPTIMAL
# here we sort the dep array then check both arrays
# point a ptr on arr and another one on dep
# if it move on arr c+=1 and move on dep c-=1
# CONFUSE---💀💀⚡⚡⚡⚡⚡⚡ 
# Tc-O(2n) 
def minNoPlatformRailwayI(arr:list,dep:list):
    dep.sort()
    arr.sort()
    i=0
    j=0
    c=0
    maxC=0
    while(i<len(arr) and j< len(dep)):
        if arr[i]<=dep[j]:
            c+=1
            i+=1
        else:
            c-=1
            j+=1
        maxC=max(maxC,c)
    return maxC




if __name__=="__main__":
    a=[1,2,3,4]
    d=[4,1,1,1]
    p=[40,10,40,30]
    a1=[6,3,4,2,5,8,1,7]
    d1=[2,6,6,5,4,2,4,2]
    p1=[80,70,65,60,25,22,20,10]
    # print(jobScheduingProblem(a1,d1,p1))
    # print(jobScheduingProblem(a,d,p))
    start=[0,3,1,5,5,8]
    end=[5,4,2,9,7,9]
    # print(nMeetingOneRoom(start,end))
    intervals=[(1,2),(2,3),(3,4),(1,3)]
    intervals=[(0,5),(3,4),(1,2),(5,9),(5,7),(7,9)]
    # print(nonOverlappingIntervals(intervals))
    aaa=[1,2,34,5]
    # aaa.remove(2)
    aaa.insert(1,432)
    # print(aaa)
    intervals=[[1,3],[6,9]]
    newintervals=[2,5]
    intervals=[[1,2],[3,4],[7,7],[8,10],[12,16]]
    newintervals=[5,6]
    # print(insertIntervals(intervals,newintervals))
    arr=[900,945,955,1100,1500,1800]
    dep=[920,1200,1130,1150,1900,2000]
    print(minNoPlatformRailwayI(arr,dep))