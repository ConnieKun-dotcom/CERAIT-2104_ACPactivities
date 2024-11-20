def proper_divisors(n):
    if n < 1:
        return []  
    
    divisors = []  
    for i in range(1, n // 2 + 1):  
        if n % i == 0:  
            divisors.append(i)  
            
    return divisors  

def is_perfect_number(num):
    """Check if a number is a perfect number."""
    if num < 1:
        return False  

    sum_of_divisors = sum(proper_divisors(num))  # Calculate the sum of proper divisors
    return sum_of_divisors == num  # Check if the sum of divisors equals the number

def main():
    while True:
        user_input = input("Enter a number: ")
        
        try:
            number = int(user_input)  # Convert input to an integer
            if is_perfect_number(number):
                print(f"{number} is a perfect number.")
            else:
                print(f"{number} is not a perfect number.")
        
        except ValueError:
            print("Enter a valid integer.")  # Handle non-numerical input


if __name__ == "__main__":
    main()