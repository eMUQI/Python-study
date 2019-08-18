import string

current_user = ["user"+i for i in string.ascii_uppercase[:5]]
current_user_lowwer = [s.lower() for s in current_user]

new_user = ["user"+i for i in string.ascii_uppercase[3:8]]

# print(current_user)
# print(new_user)

for user in new_user:
    if user.lower() in current_user_lowwer:
        print("Need a new username!")
    else:
        print("username is good!")