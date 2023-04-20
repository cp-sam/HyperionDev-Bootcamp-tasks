'''The program below functions as a simple calculator and handles user errors encountered during its runtime. 
It requests 2 numbers from the user and a preferred mathematical operator from the list shown below, to perform the calculation.
It goes further to review the user's previous calculations when 'read' is typed.'''

try:
    run_calculator = True
    while run_calculator:
        print("Welcome to calculator_x! Calculator_x performs the following operations:")
        print("'+' = addition, '-' = subtraction, '*' = multiplication")
        print("'/' = division, '**' = exponential, '%' = modulus (returns the remainder when the first number is divided by the second number.)")
        
        print("\nNOTE: PLEASE ENSURE YOU HAVE PREVIOUS CALCULATIONS STORED BEOFRE TYPING 'READ'. Otherwise, please type 'calc' below.")
        select = input("\nPlease, type 'calc' to make a calculation, or 'read' to review previous calculations: ").lower()
        
        if select == "calc":   
            start_calculation = True
            
            while start_calculation:
                try:
                    num_input1 = float(input("please enter your first number: "))
                    operator1 = input("select one of the following operators for your calculation (+, -, *, /, **, and %): ")
                    '''I used an if condition to handle wrong operator selection so that the user is prompted early of the error
                    Time is the basis of my idea here, instead of waiting for all selections, errors are corrected early.'''
                    # This handles and corrects operator errors
                    if operator1 not in ["+", "-", "*", "/", "**", "%"]:
                        print("Sorry, this calculator only computes '+, -, *, /, **, %'. Try again")
                        continue
                    
                    num_input2 = float(input("please enter your second number: "))

                    output = ""
                    
                    if operator1 == "+": # Addition
                        output = num_input1 + num_input2
                    elif operator1 == "-": # Subtraction
                        output = num_input1 - num_input2
                    elif operator1 == "*": # Multiplication
                        output = num_input1 * num_input2
                    elif operator1 == "/": # Division
                        output = num_input1 / num_input2
                    elif operator1 == "**": # Exponential
                        output = num_input1 ** num_input2
                    elif operator1 == "%": # Modulus
                        output = num_input1 % num_input2
                        
                    print(f"You have selected \n{num_input1} {operator1} {num_input2}")
                    print(f"Your answer is {output:.2f}")
                    
                    with open("user_equations.txt", "a") as text:
                        text.write(f"{num_input1} {operator1} {num_input2} = {output:.2f}\n")
                    
                    while True:
                        check = input("Do you want to perform another calculation? Type 'y' to continue or 'n' to stop: ").lower()
                        if check == "y":
                            break
                        elif check == "n":
                            start_calculation = False
                            break
                        else:
                            print("Sorry, you must enter either 'y' or 'n'. Try again")
                except ValueError:
                    print("Please enter only numerical values")
                except ZeroDivisionError:
                    print("Sorry, you cannot divide by 0. Please enter a non-zero value.")
        # I wanted the user to be re-directed to the first prompting after 'n' has been selected.
        # This provides a chance to read the review the calculations without ending the program.          

        elif select == "read":
            while True:
                read_calc = input("Please enter the name of the file as 'text', to review previous calculations: ").lower()
                
                if read_calc == "text":
                    try:
                        with open("user_equations.txt", "r") as text:
                            read_text = text.readlines()
                            for reveal in read_text:
                                print(reveal)
                        break
                                
                    except FileNotFoundError:
                        print("Sorry, this file name does not exist. Try again")
                    except PermissionError:
                        print("Sorry, you don't have permission to access this file. Try again")
                else:
                    print("You have not entered a valid file name. Please try again.")
                    
        elif not select.isalpha():
            print("\nSorry, numerical values are not allowed at this point. Try again\n")
            
        else:
            print("\nYou have not selected a valid input. Try again.\n")
            
except FileNotFoundError:
    print("\nThis file does not exist")
except KeyboardInterrupt:
    print("\nYou have successfully stopped the calculator")
