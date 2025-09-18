import sys

def main():
    """Print first command-line argument."""
    if len(sys.argv) < 2:
        print("None.")
    else:
        print(sys.argv[1])
main()
