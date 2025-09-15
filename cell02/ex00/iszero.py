"""Check if a number is zero in Python."""

def main():
    """This function is the main function."""

    num = float(input("Enter a number: "))
    text_result = "This number is equal to zero." if num == 0.0 else "This number is different from zero."
    print(text_result)
main()
