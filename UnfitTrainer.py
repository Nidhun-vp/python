values=[]

for i in range(9):
    values.append(int(input()))
    
avg1=(values[0]+values[3]+values[6])//3    
avg2=(values[1]+values[4]+values[7])//3  
avg3=(values[2]+values[5]+values[8])//3  

max_avg=max(avg1,avg2,avg3)

if max_avg<70:
    print("all trainees are unfit!!")
else:
    if avg1==max_avg:
        print("TRAINEE NO 1")
    if avg2==max_avg:
        print("TRAINEE NO 2")   
    if avg3==max_avg:
        print("TRAINEE NO 3")     