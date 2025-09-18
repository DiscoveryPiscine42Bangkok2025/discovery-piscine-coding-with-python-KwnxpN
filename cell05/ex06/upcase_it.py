import sys

def main():
    """Print system arguments in uppercase."""
    if len(sys.argv) != 2:
       print("None.")
       return
    print(sys.argv[1].upper())
main()
