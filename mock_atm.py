username = input("Enter your username? \n")
allowedUsers= ["Seyi", "Mike", "Cynthia"]
allowedPassword = ["seyi", "mike", "cynthia"]

if (username in allowedUsers):
    password = input("input your password \n")
    UserId = allowedUsers.index(username)
    
    if (password == allowedPassword[UserId]):
        print("Welcome %s" % username)

        import datetime
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(currentTime)
        
        balance = 5000
        print("Account Balance: %d NGN" %balance)
        print("What do you want to do?")
        print("1.   Withdrawal")
        print("2.   Deposit")
        print("3.   Complaint")

        selectedOption = int(input("Please select an option \n"))

        if (selectedOption == 1):
            print("You selected %d" %selectedOption)
            amount = int(input("How much would you like to withdraw? \n"))
            if (amount > balance):
                print("Insufficient Balance, \nYou only have %d NGN in your account" %balance )
            elif (amount < 0):
                print("Invalid Input, Try Again")
            elif (amount == 0):
                print("Invalid Input, Put an amount")
            else:
                print("Withdrawal Sucessful! you just withdrew %d NGN. Take your Cash" %amount)
                currentBal = int(balance - amount)
                print("Current Balance: NGN %d" %currentBal)

            
            
 
        elif (selectedOption == 2):
            print("You selected %d" %selectedOption)
            amount = int(input("How much would you like to deposit? \n"))
            if (amount < 0):
                print("Invalid Input, Please Try Again")
            elif (amount == 0):
                print("You haven't inputted any value, Please try again")
            else:
                print("Deposit Sucessful! you just deposited %d NGN" %amount)
                currentBal = int(balance + amount)
                print("Current Balance: NGN %d" %currentBal)

            
            

        elif (selectedOption == 3):
            print("You selected %d" %selectedOption)
            input("What issue will you like to report? \n")
            print("Thanks for contacting us")

        else:
            print("Invalid option selected, Please try again")
    else:
        print("Password incorrect, Try Again or Request from your Admin")
else:
    print("Username not found")