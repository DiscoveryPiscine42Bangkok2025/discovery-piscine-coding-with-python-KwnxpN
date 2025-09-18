import sys

def main():
    """Get 2 number arguments and print array of all numbers in range [min, max]."""
    if len(sys.argv) != 3:
        print("None.")
        return
    min_val = int(sys.argv[1])
    max_val = int(sys.argv[2])
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    print(list(range(min_val, max_val + 1)))
main()
