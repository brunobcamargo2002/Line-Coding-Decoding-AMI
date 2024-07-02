import csv

def generate_pattern_functions():
    pattern_map = {}
    binary_map = {}

    # Read the CSV file
    with open('table.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            binary_string = row[0]
            pattern = row[1]
            pattern_map[binary_string] = pattern
            binary_map[pattern] = binary_string

    # Generate the function to get pattern from binary
    def get_pattern_from_binary(binary_string):
        if binary_string in pattern_map:
            return pattern_map[binary_string]
        else:
            return "Pattern not found for input binary string."

    # Generate the function to get binary from pattern
    def get_binary_from_pattern(pattern):
        if pattern in binary_map:
            return binary_map[pattern]
        else:
            return "Binary string not found for input pattern."

    return get_pattern_from_binary, get_binary_from_pattern

# # Generate the functions
# pattern_to_pattern, pattern_to_binary = generate_pattern_functions()

# # Example usage
# binary_input = "000100010101001101010000"
# result_pattern = pattern_to_pattern(binary_input)
# print(f"The pattern corresponding to binary '{binary_input}' is '{result_pattern}'")

# pattern_input = "-0-0++-+-++0+--+0+"
# result_binary = pattern_to_binary(pattern_input)
# print(f"The binary corresponding to pattern '{pattern_input}' is '{result_binary}'")
