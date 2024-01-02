def min_diff(arr):
    arr=sorted(arr)
    size=len(arr)
    min_diff=9999*999
    for i in range(size-1):
        if(arr[i+1]-arr[i]<min_diff):
            min_diff=arr[i+1]-arr[i]
    return min_diff 
    
arr=[5,32,45,4,12,18,25]
print("minimum difference b/w elements of array:",min_diff(arr))    