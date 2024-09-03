def classify_age(age):
    if age < 0 or age > 150:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 35:
        return "Young Adult"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

def classify_and_print_age():
    age = int(input("Enter your age: "))
    age_category = classify_age(age)
    print(age_category)
    if age_category == 'Invalid age':
        print("Please enter a valid age.")
    else:
        print("You are classified as:", age_category)

classify_and_print_age()
