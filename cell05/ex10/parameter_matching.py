import sys

def main():
    """get argument and check equality with input"""
    if len(sys.argv) != 2:
        print("None.")
        return
    to_compare = input("What was the parameter? : ")
    if sys.argv[1] == to_compare:
        print("Good job!")
    else:
        print("Nope, sorry...")
main()
