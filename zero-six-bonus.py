def maxi_number(*args):
    maximum = 0
    index = 0
    for i in args:
        index += 1
    for j in range(0,index):
        if args[j] >= maximum:
            maximum = args[j]    

    return maximum

             
        

        


