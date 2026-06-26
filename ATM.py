balance = int(input("How much balance do you want?:"))
password = int(input("your password:"))
def check_password():
    return int(input("Please enter your password:"))

def menu():
     return int(input("1=check balance 2=add balance 3=withdrawal of money 4=exit:"))
while True:
    user = menu()
    if user not in (1, 2, 3, 4):
        print("please choose a number between 1 and 4")
    elif user == 1:
        if check_password() == password:
            if balance > 0:
                print(f"Your balance is:{balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Your password is incorrect!")
    elif user == 2:
        if check_password() == password:
            add_balance = int(input("Add balance:"))
            balance = balance + add_balance
        else:
            print("Your password is incorrect!")
    elif user == 3:
        if check_password() == password:
            if balance > 0:
                withdrawal = int(input("withdrawal of money:"))
                balance = balance - withdrawal
            else:
                print("Insufficient balance!")
        else:
            print("Your password is incorrect!")
    elif user == 4:
        break
    