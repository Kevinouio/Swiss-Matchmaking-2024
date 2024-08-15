# Function to get a non-empty string input
def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please try again.")


# Function to get a valid integer input
def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            else:
                print("Input must be a positive integer. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
