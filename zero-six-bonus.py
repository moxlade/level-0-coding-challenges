def maxi_number(*args):
    max = 0
    index = 0
    for i in args:
        index += 1
    for j in range(0,index):
        if args[j] >= max:
            max = args[j]    

    return max

             
        
    
        


