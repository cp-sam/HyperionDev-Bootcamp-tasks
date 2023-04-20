# HyperionDev-Bootcamp-task 4
This contains the 4th task of my HyperionDev Data Science Bootcamp testing my understanding of logical operators.

# This program belowasssesses participants in a triathlon and rewards them based on their total completion time
award1 = "Provincial Colours award"
award2 = "Provincial Half Colours award"
award3 = "Provincial Scroll award"
award4 = "No award"

# Got the idea about splitting the individual triathlon events from a friend.
swimming_time = int(input("Please enter the participant's swimming time in minutes: "))
cycling_time = int(input("Please enter the participant's cycling time in minutes: "))
running_time = int(input("Please enter the participant's running time in minutes: "))
total_time = swimming_time + cycling_time + running_time
qualifying_time = 100

# I used comparison logical operators to limit the times to fit the corresponding if/elif/else conditions.
if total_time == qualifying_time:
    print(f"Congratulations Participant! you finished in {total_time} minutes and will receive a" + " " + award1)
    
elif (total_time >= qualifying_time) and (total_time < (qualifying_time + 6)):
    print(f"Congratulations Participant! you finished in {total_time} minutes and will receive a" + " " + award2)

elif (total_time >= qualifying_time) and (total_time < (qualifying_time + 11)):
    print(f"Congratulations Participant! you finished in {total_time} minutes and will receive a" + " " + award3)

elif (total_time >= qualifying_time + 11):
    print(f"Dear Participant, you finished in {total_time} minutes. Unfortunately you will receive" 
          + " " + award4 + ". " + "Better luck next time")
    
else:
    print("Dear Participant, you have not completed all 3 stages of the triathlon.")
