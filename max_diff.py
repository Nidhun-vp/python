def max_diff_ele(arr):
    arr=sorted(arr)
    size=len(arr)
    max_diff=-999*999
    for i in range(size-1):
        if(arr[i+1]-arr[i]>max_diff):
            max_diff=arr[i+1]-arr[i]
    return max_diff 
    
arr=[5,32,45,4,12,18,25]
print("maximum difference b/w elements of array:",max_diff_ele(arr))    