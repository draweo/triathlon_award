# this program determines the award a person 
# competing in a triathlon will receive

# ask user in input their finish time for each individual event
# converting input to integers
print()             # de-clutter, add a blank line
time_swim = int(input("SWIM finish time (mins): "))
time_cycle = int(input("CYCLE finish time (mins): "))
time_run = int(input("RUN finish time (mins): "))
print()             # de-clutter, add a blank line

# calculate the total time for all three race segments, combined.
total_time = (time_swim + time_cycle + time_run)
print (f"Your triathlon finishing time is {total_time} minutes.")         
print()             # de-clutter, add a blank line

# for combined/total times of 100 mins or less, award Provincial Colours
if (total_time <= 100):
    print("Congratulations! You have achieved Provincial Colours!")

# for combined/total times of 101-105 mins, award Provincial Half Colours  
elif (total_time <= 105):
    print("Great race! You are awarded Provincial Half Colours.")

# for combined/total times of 106-110 mins, award Provincial Scroll  
elif (total_time <= 110):
    print("Great effort! You are awarded a Provincial Scroll.")

# for times of 111 mins or more, no award is given 
else:
    print("Unfortunately, you just missed out on the awards.")
print()             # de-clutter, add a blank line
