import sys

def main():
    """Scan and find the first argument in second argument"""
    if len(sys.argv) != 3:
        print("None.")
        return
    
    count = sys.argv[2].count(sys.argv[1])
    print(count)
main()
