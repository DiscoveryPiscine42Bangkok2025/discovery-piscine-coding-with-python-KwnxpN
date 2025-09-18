import sys

def main():
    """add 'ism' to all arguments if argument not ends with 'ism' """
    if len(sys.argv) < 2:
       print("None.")
       return
    for arg in sys.argv[1:]:
        if not arg.lower().endswith("ism"):
            print(arg + "ism")
main()
