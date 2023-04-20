# The program below keeps requesting number input from a user until "-1" is entered.
# It goes further to calculate the average of the values entered excluding "-1"

user_list = []

while True:

    try:
        user_num = input("Please enter a number: ")
        
        # I used if statements and try/except to catch possible user errors 
        if user_num == "":
            print("You have not entered any value. Try again")
            continue
            
        if user_num < "0" and user_num != "-1":
            print("You have entered negative numbers asides '-1'. Try again")
            continue
    
        if user_num == "-1":
            break
    # I used the append method below to add numbers that are not equal to -1 to the user_list.
    # The else statement below was not necessary, however, I used it to improve understanding and readability of why -1 is not included
        else:
            lists = user_list.append(int(user_num))   
    
    except ValueError:
        print("Invalid input, please enter only numerical integers e.g 3")
 
try:    
    average = sum(user_list) / len(user_list) 
    print(f"\nThe average of the numbers entered is: {average}")
    
except ZeroDivisionError:
    print("You have entered '-1' without entering the numbers to be averaged. Try again") 
