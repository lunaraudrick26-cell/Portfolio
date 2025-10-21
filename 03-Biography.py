# Exercise 3: Biography - 25 Marks
# Store and print name, hometown, and age using a dictionary

# Advanced Requirements: User input with validation
name = input("Enter your name (first and last): ")
hometown = input("Enter your hometown: ")

# Validate age input to ensure it's a number
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for age.")

# Store information in a dictionary
biography = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print values on separate lines using a single print statement
print(f"Name: {biography['name']}\nHometown: {biography['hometown']}\nAge: {biography['age']}")

# Note: Using input() handles multiple words automatically
# Using isdigit() prevents string values for age