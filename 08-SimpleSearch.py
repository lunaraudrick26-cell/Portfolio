# Exercise 8: Simple Search - 30 Marks
# Search for a specific string within a list

# Initialize list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Optional Requirement: Allow user input for search term
search_name = input("Enter a name to search for: ")

# Search for the name in the list
if search_name in names:
    print(f"{search_name} found in the list!")
    # Get the index position
    position = names.index(search_name)
    print(f"{search_name} is at position {position}.")
else:
    print(f"{search_name} not found in the list.")

# Display all names in the list
print(f"\nAll names in the list: {', '.join(names)}")