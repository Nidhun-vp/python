def rain_trap():
    size=len(arr)
    left=size*[0]
    right=size*[0]
    water=0
    max_so_far_left=arr[0]
    #for left array
    for index in range(0,size):
        if(max_so_far_left<arr[index]):
            max_so_far_left=arr[index]
            left[index]=max_so_far_left
        else:
            left[index]=max_so_far_left

    #for right array
    max_so_far_right=arr[-1]
    for index in range(size-1,-1,-1):
        if(max_so_far_right<arr[index]):
            max_so_far_right=arr[index]
            right[index]=max_so_far_right
        else:
            right[index]=max_so_far_right       
    print(arr)         
    print(left)
    print(right)
    #fill water
    for index in range(0,size):
        water=water+min(left[index],right[index])-arr[index]
    return(water)
            
                
    
    
arr=[1,0,2,0,1,0,3,1,0,2]    
print(rain_trap())
