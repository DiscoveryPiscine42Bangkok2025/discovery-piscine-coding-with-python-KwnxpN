"""Loop until number hit 25 in Python."""

def main():
    """This function is the main function."""

    num = int(input("Enter a number less than 25 : "))
    if num > 25: return print("Error") # Error casse more than 25

    while num <= 25:
        print(f"inside the loop, my variable is {num}")
        num += 1
main()
