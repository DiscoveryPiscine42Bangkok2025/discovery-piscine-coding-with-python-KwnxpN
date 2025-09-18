import sys

def main():
    """Print system arguments in lowercase."""
    if len(sys.argv) != 2:
       print("None.")
       return
    print(sys.argv[1].lower())
main()
