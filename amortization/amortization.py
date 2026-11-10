# Monthly Amortization Calculator Program
# 
# This program intends the following:
# 1. Get a loan ammount from the user, loan term (years and months), interest rate
# 2. Compute the monthly payment and generate the payment schedule
# 3. Output to user the following:
#    a. The amortization schedule table
#    b. Total payments made, and total interest for the entire term, with pie chart
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
print("|                    SIMPLE AMMORTIZATION CALCULATOR                         |")
print("******************************************************************************")

is_true = True

print("Enter [C] to calculate monthly payment")
print("Enter [X] to exit calculator")

while is_true == True :
    flag = input("   >>> ")

    if flag.upper() == "C":
        p = float(input("   | Loan Amount (Php): >>> "))
        r = float(input("   | Annual Interest Rate (%): >>> ")) * 0.01 / 12.00 
        n = int(input("   | Payment term length (months): >>> "))
        m = float(p * ( ( r * ((1 + r) ** n)) / (((1 + r) ** n) - 1) ))
        end_bal = p
        print(f"   |\n   | Your monthly payment (Php): >>> {round(m, 2)}\n   |")
        print("   |-----------------------------------------------|")
        print("   |            AMMORTIZATION SCHEDULE             |")
        print("   |-----------------------------------------------|")
        print("   | Month | Interest | Principal | Ending Balance |")
        print("   |-----------------------------------------------|")
   
        for i in range(1,n+1):
            interest = round(float(end_bal * r ), 2)
            p_due = float( m - interest )
            end_bal = float( end_bal - p_due )
            print(f"   |   {i} | {interest} | {p_due} | {end_bal}")

        print("   |")
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

    
