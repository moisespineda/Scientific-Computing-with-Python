def add_time(start_time, duration, day=""):

    #process to convert from 12 hours format to 24 hours formar
    time=start_time.split()
    hour_min=time[0].split(":")
    end=time[1]

    if time[1]=="PM":
        hour=int(hour_min[0])+12
        hour_min[0]=str(hour)
    
    duration_time=duration.split(":")

    #add the duration to the 24 hours format hours and minutes 
    new_hour=int(hour_min[0])+int(duration_time[0])
    new_minutes=int(hour_min[1])+int(duration_time[1])

    #conditional to evaluate if adding the minutes we get in a new hour
    if new_minutes>=60:
        extra_hour=new_minutes//60
        new_minutes-=extra_hour*60
        new_hour+=extra_hour

    #conditional to evaluate if adding the hours we get in a new day
    extra_day=0
    if new_hour>24:
        extra_day=new_hour//24
        new_hour-=extra_day*24

    #conditional to retur to the 12 hours format
    if new_hour>0 and new_hour<12:
        end="AM"
    elif new_hour==12:
        end="PM"
    elif new_hour>=12:
        end="PM"
        extra_hour-=12
    else:
        end="AM"
        new_hour+=12

    #conditional for adding an next day or x days later message
    if extra_day>0:
        if extra_day==1:
            day_later=(" (next day)")
        else:
            day_later=" (" + str(extra_day) + " days later)"
    else:
        day_later=""

    #conditional for returning the new day if the user give the starting day to function
    week_days=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if day:
        weeks=extra_day//7
        i=week_days.index(day.lower().capitalize())+(extra_day-7*weeks)
        if i>6:
            i-=7
        day=", "+week_days[i]
    else:
        day=""

    #we define the new_time format for returning
    new_time=str(new_hour)+":"+\
        (str(new_minutes) if new_minutes>9 else ("0" + str(new_minutes))) + \
        " " + end + day + day_later

    return new_time



