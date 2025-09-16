"""Generate a multiplication table."""

def multiplication_table(n):
    """Generate a multiplication table up to n x 10."""
    print(f"Table de {n}", end=": ")
    mult_counter = 0
    while mult_counter <= 10:
        print(f"{n * mult_counter}", end=" ")
        mult_counter += 1
    print() # for new line

def main():
    """Print the multiplication table."""
    couter = 0
    while couter <= 10:
        multiplication_table(couter)
        couter += 1
main()
