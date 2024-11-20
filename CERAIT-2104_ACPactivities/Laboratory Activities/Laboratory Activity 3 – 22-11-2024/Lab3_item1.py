def roman_to_integer(roman):
    # Dictionary to map Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0  
    prev_value = 0  

    # Iterate through each character in the Roman numeral string from right to left
    for char in reversed(roman):
        current_value = roman_values[char]  
        
        # If the current value is less than the previous value, we have a subtractive case
        if current_value < prev_value:
            total -= current_value  
        else:
            total += current_value  
        
        prev_value = current_value  

    return total  

def get_roman_input():
    while True:
        user_input = input("Enter a Roman numeral: ").strip().upper()
        if all(char in "IVXLCDM" for char in user_input):  # Validate input
            return user_input
        else:
            print("Invalid input. Please enter a valid Roman numeral.")


roman_numeral = get_roman_input()
result = roman_to_integer(roman_numeral)
print(f"The integer value of \'{roman_numeral}\' is: {result}")