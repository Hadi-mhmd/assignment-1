username = input("enter your username: ")
password = input("enter your password: ")

if username=="admin" and password=="1234":
    print(f"Access granted for {username}")
else:
    print(f"Access denied for {username}")    