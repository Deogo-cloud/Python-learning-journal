username = "deogo"
password = "deogo123"
login_username = input("Enter username:")
login_password = input("Enter password:")
if login_username == username and login_password == password:
    print("Login sucessful!")
else:
    print("Login failed!")
age = int(input("enter your age:"))
if age >= 18 and age <= 30:
    print("eligible age")
else:
    print("not eligible")
