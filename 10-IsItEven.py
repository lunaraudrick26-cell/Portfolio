# Exercise 10: Is it even? - 35 Marks
# Test if a value is even or odd using functions

def check_even_odd(number):
    """
    Function to determine if a number is even or odd
    
    Args:
        number: Integer to check
    
    Returns:
        String message indicating if number is even or odd
    """
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    """
    Main function to get user input and display result
    """
    # Ask user for a number
    try:
        user_number = int(input("Enter a number: "))
        
        # Pass number to function and get result
        result = check_even_odd(user_number)
        
        # Print the message returned by the function
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
if __name__ == "__main__":
    main()