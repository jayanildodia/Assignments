# Create a login page backend to ask users to enter the username
# and password. Make sure to ask for a Re-Type Password and if the
# password is incorrect give a chance to enter it again but it should
# not be more than 3 times.

def login():
    passwd = input("Type a Password: ")
    counter = 3
    while counter > 0:
        newpasswd = input("Type the password again: ")
        if newpasswd == passwd:
            print("Approved")
            return
        else:
            counter -= 1
            if counter == 0:
                print("Login Unsuccessful")
            else:
                print("Try again!")

username = input("choose a username without spaces inbetween: ")
login()
