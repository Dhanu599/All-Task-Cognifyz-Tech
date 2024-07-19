def Validate(email):
    if "@" in email and "." in email.split("@") [-1]:
        return True
    else:
        return False
    
    email = input("Enter the mail to Validate:")
    Value = Validate(email)

    if (value == True):
        print("You Enter the Correct Mail.....")

    else:
        print("You Enter the Wrong Mail....")
