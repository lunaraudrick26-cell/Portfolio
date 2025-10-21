# Exercise 4: Primitive Quiz - 30 Marks
# Quiz program with multiple questions and case-insensitive answers

# Dictionary of European countries and their capitals
quiz_data = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Poland": "Warsaw"
}

score = 0

print("European Capitals Quiz")
print("=" * 40)

# Loop through each country and ask for its capital
for country, capital in quiz_data.items():
    answer = input(f"What is the capital of {country}? ")
    
    # Check answer (case-insensitive)
    if answer.lower() == capital.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {capital}.\n")

# Display final score
print("=" * 40)
print(f"Quiz complete! Your score: {score}/{len(quiz_data)}")