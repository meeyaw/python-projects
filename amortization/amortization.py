# Monthly Amortization Calculator Program
# 
# This program intends the following:
# 1. Get a loan ammount from the user, loan term (years and months), interest rate
# 2. Computes the monthly payment
# 3. Output to user the following:
#    a. The amortization schedule table
#    b. Total payments made, and total interesr for the entire term, with pie chart
# 4. The program should be a gui for the user.
#
# Formula for Amortization:
#
#              r [( 1 + r ) ^ n]
#   M = P x ----------------------- 
#             [( 1 + r ) ^ n ] - 1
# 
#  where:
#     M = monthly payment
#     P = loan amount
#     r = Monthly interest rate ( annual interest rate / 12 )
#     n = no of payments, in months
# 
print("******************************************************************************")
print("********************* SIMPLE AMMORTIZATION CALCULATOR ************************")
print("******************************************************************************")

is_true = True

print("Enter [C] to calculate monthly payment")
print("Enter [X] to exit calculator")

while is_true == True :
    flag = input("   >>> ")
    if flag.upper() == "C":
        p = float(input("   | Loan Amount (Php): >>> "))
        r = float(input("   | Annual Interest Rate (%): >>> ")) / 100 / 12 
        n = int(input("   | Payment term length (months): >>> "))
        m = float(p * ( ( r * ((1 + r) ** n)) / (((1 + r) ** n) - 1) ))
        print(f"   |\n   | Your monthly payment (Php): >>> {round(m, 2)}\n   |")
        print("Enter [X] to exit")
    elif flag.upper() == "X":
        print("Exiting ...")
        break
    else:
        print("Error. Invalid choice.\n")
        print("Enter [C] to calculate monthly payment")
        print("Enter [X] to exit calculator")

print("******************************************************************************")
print("************* Thank you for using the Amortization Calculator ****************")
print("******************************************************************************")

    
