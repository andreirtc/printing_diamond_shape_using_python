# Create a function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character. 
def print_diamond(n):
    if n % 2 == 0:
        return "Please provide an odd integer."
    
    for i in range(n):
        spaces = abs(n // 2 - i)
        stars = n - 2 * spaces
        print(" " * spaces + "*" * stars)
print_diamond(5)