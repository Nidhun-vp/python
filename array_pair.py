def sumpair(arr,target):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<=right):
        if(arr[left]+arr[right]>target):
            right=right-1
        elif(arr[left]+arr[right]<target):
            left=left+1    
        elif(arr[left]+arr[right]==target):
            print("array pairs are:",arr[left],"&",arr[right])
            right=right-1
            left=left+1     
    
    
    
    
    
    
arr=[5,7,4,3,9,8,19,11]
target=17  
sumpair(arr,target) 