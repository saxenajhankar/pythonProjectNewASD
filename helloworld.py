# ASD Assignment 1 - setting up IDE
import sys

# Check if the number of command-line arguments is less than 2
if len(sys.argv) < 2:
    # Print an error message if no names are provided
    print("Error: Provide at least one name!")
else:
    # Iterate over each name provided as a command-line argument
    for name in sys.argv[1:]:
        # Print a greeting for each name
        print(f"Hello, {name}!")