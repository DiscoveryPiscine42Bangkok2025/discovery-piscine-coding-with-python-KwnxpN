"""Check number positive, negative, or zero after multiple in Python."""

def number_check(num):
    """Check if number is positive, negative, or zero."""
    if num > 0:
        return "This result is positive."
    elif num < 0:
        return "This result is negative."
    else:
        return "This result is positive and negative."
    
def main():
    """This function is the main function."""
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 * num2
    print(f"{num1} x {num2} = {num1*num2}\n{number_check(result)}")
main()
