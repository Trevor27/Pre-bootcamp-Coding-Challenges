def convert_time(time):
    
    hour = time // 60

    time %= 60

    minutes = time

    if hour <= 1:
        print(str(hour) + " hour, " + str(minutes) + (" minutes"))

    else:
        print(str(hour) + " hours, " + str(minutes) + (" minutes"))

convert_time(122)
