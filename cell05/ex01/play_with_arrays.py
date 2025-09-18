"""Copy an array and plus 2 to each element."""

def main():
    """Copy an array and plus 2 to each element."""
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    copy = [x + 2 for x in original]
    print(copy)
main()
