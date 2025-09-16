"""Check if it is float or integer."""

def main():
    """Check if it is float or integer."""
    num = float(input("Give me a number: "))
    if num % 1 != 0:
        print(f"This number is a decimal.")
    else:
        print(f"This number is an integer.")
main()
