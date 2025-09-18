import sys

def main():
    """Print all arguments in reverse order"""
    for arg in reversed(sys.argv[1:]):
        print(arg)
main()
