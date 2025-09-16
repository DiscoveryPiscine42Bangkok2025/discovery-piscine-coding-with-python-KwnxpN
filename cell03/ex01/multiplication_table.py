"""Generate a multiplication table."""

def main():
    """Print the multiplication table."""
    num = int(input("Enter a number to generate its multiplication table: "))
    for i in range(13):
        print(f"{i} x {num} = {num * i}")
main()
