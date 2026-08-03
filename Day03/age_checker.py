age = int(input("Enter the age:"))


if age < 0:
    print("Invalid age!")
elif age < 12:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 40:
    print("You are an adult")
elif age < 60:
    print("You are middle-age")
elif age < 140:
    print("You are old")
else:
    print("You are immortal!")
