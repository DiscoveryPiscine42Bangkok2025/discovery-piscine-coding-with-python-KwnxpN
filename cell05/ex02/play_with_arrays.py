"""Copy an array and plus 2 to each element only when element value is greater than 5."""

def main():
    """Copy an array and plus 2 to each element only when element value is greater than 5."""
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    copy = []
    for i in original:
        if i > 5:
            copy.append(i + 2)
    print(copy)
main()
