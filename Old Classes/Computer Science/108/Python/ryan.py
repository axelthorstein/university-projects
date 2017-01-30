#How fast was our marathon? 
hours = 4
minutes = 1

# convert our time to Paul Ryan time (70% of real time) 
time_in_minutes = hours * 60 + minutes
ryan_time_in_minutes = time_in_minutes * 0.7

#convert back to hours and minutes
ryan_hours = ryan_time_in_minutes // 60
ryan_minutes = ryan_time_in_minutes % 60

#report the results
print("Your Ryan time is : ")
print("Hours", ryan_hours)
print("Minutes", ryan_minutes)

    