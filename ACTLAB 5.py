def classify_age(age):
    if age < 0:
        print("invalid age, it cannot be negative.")
    elif age <= 12:
        print("You are a child")
    elif age <= 19:
        print("You are a teen")
    elif age <= 64:
        print("You are an adult")
    else:
        print("You are a Senior")
        
while True:
    age = int(input("Enter your age: "))
    classify_age(age)