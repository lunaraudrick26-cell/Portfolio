# Exercise 6: Brute Force Attack - 30 Marks
# Password entry system with maximum attempts

# Define correct password
correct_password = "12345"

# Maximum number of attempts (optional requirement)
max_attempts = 5
attempts = 0

# Loop until correct password or max attempts reached
while attempts < max_attempts:
    password = input("Enter the password: ")
    attempts += 1
    
    if password == correct_password:
        print("Access granted! Welcome.")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) remaining.")
        else:
            print("Maximum attempts reached. The authorities have been alerted!")
            break