import csv

def main():
    print("\n Do you want to create an account or to login ?: \n")
    a = input("1. To create an account or 2. to login, 3. To exit : ")
    if a == "1":
        create_account()
    if a == "2":
        login()
    if a == "3":
        print("Exiting ...")
    elif a != "1" and a!= "2":
        print("something wrong happened")
        main()

def create_account():
    f = open("login.txt", "a")
    print("Creating account : \n")
    username = input("Username : ")
    password = input("Password : ")
    if checker(username, password):
        f.write(username + ":" + password + "\n")
        print("\n Account succefully created ! ")
        main()
    else:
        print("Something wrong happened, you must not use a comma in your password or username ")
        create_account()
def login():
    print("====Login====")

    usernames = []
    passwords = []
    with open("login.txt", "r") as f:
        for line in f:
            fields = line.strip().split(":")
            usernames.append(fields[0])  # read all the usernames into list usernames
            passwords.append(fields[1])  # read all the passwords into passwords list

            # Use a zip command to zip together the usernames and passwords to create a dict
    userinfo = zip(usernames, passwords)  # this is a variable that contains the dictionary in the 2-tuple list form
    userinfo_dict = dict(userinfo)
    print(userinfo_dict)

    username = input("Enter username: ")
    password = input("Enter password: ")
    if checker(username, password):
        if username in userinfo_dict.keys() and userinfo_dict[username] == password:
            loggedin()
        else:
            print("Access Denied\n")
            login()
    else:
        print("Something wrong happened, you must not use a comma in your password or username ")

def checker(username, password):
    if "," in username or "," in password:
        return False
    else:
        return True
def loggedin():
    print("You just logged in ! ")
main()
