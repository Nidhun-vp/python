def divide(a,denom):
    try:
       ans= a / denom
       print("result is",ans)
    except ZeroDivisionError as e:
        print("divided by 0 terminate")
    finally:
        print("division complete")  
divide(6,0)          
    
    
