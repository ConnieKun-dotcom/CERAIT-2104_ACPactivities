from Capybara import Capybara

# Predefined test cases
capybaras = [
    Capybara("Biscoff", "M", 5),
    Capybara("Caramel", "F", 3),
    Capybara("Mocha", "M", 7)
]

# Prompt user to input test case number
try:
    test_case_number = int(input("Enter the test case number: "))

    if 1 <= test_case_number <= len(capybaras):
        selected_capybara = capybaras[test_case_number - 1]
        print(f"Test Case {test_case_number}: Name: {selected_capybara.name}, "
              f"Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old")
    else:
        print("Invalid test case number. Please enter a number between 1 and 3.")

except ValueError:
    print("Invalid input. Please enter a valid test case number.")