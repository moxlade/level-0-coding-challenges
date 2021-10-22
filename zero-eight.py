def time_converter(x):
    hours = x//60
    minutes = (x % 60)
    total_time = " "
    if hours >= 2 or hours == 0:
        total_time = str(hours) + " hours, "
    elif hours == 1:
        total_time = str(hours) + " hour, "
    if minutes == 1:
        total_time = total_time + str(minutes) + " minute "
    elif minutes >= 2 or minutes == 0:
        total_time = total_time + str(minutes) + " minutes "
    
    total_time = total_time[0:-1]
    return total_time



