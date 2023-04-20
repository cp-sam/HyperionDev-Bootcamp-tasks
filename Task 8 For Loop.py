# The code below keeps requesting a user to enter number 5 and responds to user errors it encounters from wrong inputs.
# Once 5 is entered, it goes further to print asteriks in ascending order to a total of 5

while True:
    try:
        
        user = int(input("Please enter number 5: "))
        stars = ""
        if user == 5:
            for new_stars in range(5):
                stars += "*"
                print(stars)
            break

        if user != 5:
            print("Sorry user, for this task, you must enter ONLY '5'. Try again")
    except ValueError:
        print("You have not selected an integer. Try again")
