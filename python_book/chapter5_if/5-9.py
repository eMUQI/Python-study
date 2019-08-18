import string

list_of_user = ["user"+i for i in string.ascii_uppercase[:4]]
list_of_user.append("admin")

for user in list_of_user:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello %s, thank you for logging in again" % user)

del list_of_user[:]

if not list_of_user:
    print("We need find some users!")
