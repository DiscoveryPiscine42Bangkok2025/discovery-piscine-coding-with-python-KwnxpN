"""What you say?, oh STOP!"""

def main():
    """Print what you say."""
    text = input("What you gotta say? : ").upper()
    while text != "STOP":
        text = input("I got that! Anything else? : ").upper()
main()
