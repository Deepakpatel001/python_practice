# User will input (3ages).Find the oldest one

age1 = int(input("Enter the 1st age: "))
age2 = int(input("Enter the 2nd age: "))
age3 = int(input("Enter the 3rd age: "))

if age1>age2 and age1>age3:
    print(f" the oldest age is {age1}")
elif age2>age1 and age2>age3:
    print(f" the oldest age is {age2}")
else:
    print(f" the oldest age is {age3}")

    