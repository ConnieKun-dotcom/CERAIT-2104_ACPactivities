
try:
    # Input the size of the array
    size = int(input("Enter the size of the array: "))
    
    # Initialize an array with zeros
    arr = [0.0] * size
    
    # Input elements into the array
    print("Enter the elements of the array:")
    for i in range(size):
        arr[i] = float(input())

    # Ask for the index to access
    x = int(input("Enter the index of the element to print: "))
    
    # Print the element at index x with 2 decimal places
    print(f"Element at index {x}: {arr[x]:.2f}")

except IndexError:
    print(f"Index {x} is invalid")
except ValueError:
    print("Invalid input. Please enter valid numbers.")