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
            # return "Binary string not found for input pattern."
            return ""


    return get_pattern_from_binary, get_binary_from_pattern

def DC_balance(octet_string):
    dc_val=0
    for i in range(0, len(octet_string), 1):
        if octet_string[i]=='+':
            dc_val+=1
        elif octet_string[i]=='-':
            dc_val-=1
    return dc_val

def invert_pattern(pattern):
    
    stt1 = pattern.replace("+", "p")
    stt2 = stt1.replace("-","m")
    stt3 = stt2.replace("p","-")
    stt4 = stt3.replace("m","+")
    return stt4


# Function to encode a long string of octets to patterns and concatenate them
def encode_octets_to_patterns(long_octet_string):
    pattern_to_pattern, _ = generate_pattern_functions()
    
    patterns = []
    patterns_bal = []
    dc_val=0
    for i in range(0, len(long_octet_string), 8):  # Assuming octets are 8 bits each
        octet = long_octet_string[i:i+8]
        pattern = pattern_to_pattern(octet)
        dc_val+=DC_balance(pattern)
        if (dc_val >1 or dc_val<-1 ) and i >= 15:
            inv_pattern = invert_pattern(pattern)
            dc_val-=2*DC_balance(pattern)
            patterns_bal.append(inv_pattern)
        else:
            patterns_bal.append(pattern)
        patterns.append(pattern)
    
    return ''.join(patterns),''.join(patterns_bal)

def decode_patterns_to_octets(long_ternary_string):
    _,binary_map = generate_pattern_functions()
    octets = []
    for i in range(0, len(long_ternary_string), 6):  # Assuming ternary are 6 char each
        ternary = long_ternary_string[i:i+6]
        octet=binary_map(ternary)
        if octet!="":
            octets.append(octet)

        else:
            new_ternary=invert_pattern(ternary)
            new_octet=binary_map(new_ternary)
            octets.append(new_octet)
        
    return ''.join(octets)    
