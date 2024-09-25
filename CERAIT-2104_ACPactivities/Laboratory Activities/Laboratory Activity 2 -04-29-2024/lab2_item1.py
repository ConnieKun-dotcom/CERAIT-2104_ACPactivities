def is_palindrome(n):
    #convert the integer to a string to easily reverse the digits
    str_n = str(n)
    #check if the string is the same  forwards and  backwards
    if str_n  == str_n[::-1]:
        return "Palindrome"
    else:
        return   "Not a  palindrome"

#Test the function
num = int(input("Enter an integer: "))
print(is_palindrome(num))