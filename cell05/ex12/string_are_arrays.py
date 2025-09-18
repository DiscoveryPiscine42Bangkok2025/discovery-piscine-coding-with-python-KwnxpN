import sys

def main():
    """find 'z' in argument"""
    if len(sys.argv) != 2:
        print("None.")
        return
    count = sys.argv[1].count('z')
    if count == 0:
        print("None.")
        return
    print('z' * count)
main()
