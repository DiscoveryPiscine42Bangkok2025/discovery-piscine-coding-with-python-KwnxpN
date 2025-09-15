"""Is number negative in Python."""

def main():
    """This function is the main function."""

    num = float(input("Enter a number: "))
    text_result = "This number is negative." if num < 0.0 else "This number is positive."
    print(text_result)
main()
