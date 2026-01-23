# ----✔️✔️left to check
# -----SELECTION SORTING
'''
--> find the min put at first 
--> find min from left list
--> put that min at first of the left list
--> repeat 2 then 3 till get in left array length get 1
-----------
it repeats n-1 time so tc be O(n²)--> best worst avg all
'''

def selection_sorting(n:int, arr: list):
    if n==0 or n==1:
        return arr
    
    for i in range(n):
        m=arr[i]
        c=i
        for j in range(i,n):
            if m>arr[j]:
                m=arr[j]
                c=j
        new=arr[i]
        arr[i]=arr[c]
        arr[c]=new
     
            
    return arr

# a=[1,2,3,4,5]
# print(selection_sorting(5,a))




# ----BUBBLE SORTING
'''
Docstring for bubble sorting
-->compare two adjacent elements 
--> make them swap if second is smaller than first one
-->repeat steps 1 and 2 till last pair get sorted
time complexity-->best is O(N) and worst and avg is O(N²)
'''
# ---same code as striver typed
def bubble_sorting(n:int, arr:list):
    for i in range(n):
        swaps=0
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                swaps+=1
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
        if swaps==0:
            return arr
    return arr

# a=[4,252,16,243,6]

# print(bubble_sorting(5,a))

# ----INSERTION SORTING
'''
--> assume an array from starting,
--> add next element to it and position it in correct manner
--> repeat step 1 and 2 till get last element assign
--> tc=O(N²) best --> O(N)(here in this code its not there)
'''
def insertion_sorting(n:int, arr:list):
    for i in range(1,n):
        swap=0
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp
                swap+=1
    
        
    return arr

if __name__=="__main__":
    a=[14,252,16,243,6]
    print(insertion_sorting(5,a))