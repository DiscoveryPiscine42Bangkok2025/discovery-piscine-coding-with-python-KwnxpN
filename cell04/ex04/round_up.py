"""round up a number."""

def main():
    """round up a number."""
    num = float(input("Enter a number: "))
    if num % 1 != 0:
        print(int(num) + 1)
    else:
        print(int(num))
main()
