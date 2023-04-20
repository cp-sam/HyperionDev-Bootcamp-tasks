# The below program is a financial calculator that calculates expected investment proceeds
# using simple, interest, compound interest or a bond repayment plan for a house
# This is also my first trial at implementing defensive programming.


import math

print("Welcome to Finsec! Your investment and bond financial calculators.\n"
      + "\nA brief overview:"
      + "\ninvest - calculates potential interest you could earn from your investment."
      + "\nbond - calculates the amount you'll pay on a home loan.\n")

# I used a while loop, to ensure the program continues even as it spots errors and notifies the user
while True:
      calc_choice = (input("Please enter either 'invest' or 'bond' to proceed with your request: "))
      # Converts input from the user in mixed or upper cases to lower_case
      calc_choice = calc_choice.lower()
    
      if calc_choice == "invest":
            print("\nWelcome to investment calculator.")
            
            # I used nested while loops and try and except blocks, to run the program, predict possible user errors
            # and try to correct them
            while True:
                  try:
                  # I used examples to make my code more user-friendly and to help avoid possible errors
                        deposit = float(input("\nHow much will you be investing? (e.g., 12000) "))
                        rate = float(input("Enter the interest rate (do not include %) e.g., 3: "))
                        rate = rate / 100
                        time = float(input("How many years do you plan on investing? (e.g., 2) "))
                        
                       # This if condition below ensures only positive numerical values are entered.  
                        if deposit <= 0 or rate <= 0 or time <= 0:
                              print("\nYou have entered negative numerical values. Try again.")
                              continue
                        
                        while True:
                              interest = input("\nWould you like to calculate 'simple' or 'compound' interest? ")
                              interest = interest.lower()
                              
                              if interest == "simple":
                                    simple_amount = deposit * (1 + (rate * time))
                                    # I approximated the final value to 2 decimal places to avoid long complex values.
                                    print(f"\nYour total amount on investment is: {simple_amount:.2f}")
                                    break
                              
                              elif interest == "compound":
                                    compound_amount = deposit * math.pow((1 + rate), time)
                                    print(f"\nYour total amount on investment is: {compound_amount:.2f}")
                                    break 
                              
                              else:
                                    print("\nPlease enter only 'simple' or 'compound'. Try again")
                                    break
                  # I could only think of value error as a possible error in this case.                        
                  except ValueError:
                        print("Please enter only numerical values. Try again.")
                  break

      elif calc_choice == "bond":
            print("\nWelcome to bond calculator. Please enter ONLY numerical values below.")
            
            while True:
                  try:
                  # This will ensure that the program starts from the bond calculator where the error was made
                        valuation = float(input("\nPlease enter the current value of the house (e.g, 500000): "))
                        bond_rate = float(input("Enter the interest rate (e.g, 2.5): "))
                        bond_rate = (bond_rate / 100) / 12
                        bond_time = int(input("In how many months do you plan to repay the bond? (e.g, 6) "))
                        
                        
                        if valuation <= 0 or bond_rate <= 0 or bond_time <= 0:
                              print("\nYou have entered negative numerical values. Try again.")
                              continue

                        bond_repayment = (bond_rate * valuation)/(1 - (1 + bond_rate)**(- bond_time))

                        print(f"\nYour monthly bond_repayment is: {bond_repayment:.2f}")
                        break

                  except ZeroDivisionError:
                        print("\nPlease do not enter only zero (0) as a numerical value. Try again.")

                  except ValueError:
                        print("\nPrint enter only numerical values. Try again.")

# I got this idea to use .isalpha() from w3 schools
# https://www.w3schools.com/python/ref_string_isalpha.asp#:~:text=The%20isalpha()%20method%20returns,!%23%25%26%3F%20etc.
      elif not calc_choice.isalpha():
            print("\nYou have entered a numerical value. Try again.")

      else:
            print("\nPlease you must enter either 'invest' or 'bond' to proceed.")


