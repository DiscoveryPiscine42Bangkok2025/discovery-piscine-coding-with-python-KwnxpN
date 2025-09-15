"""Check if password is correct in Python."""

def main():
    """This function is the main function."""

    password = "Python is awesome"
    input_password = input("Enter the password: ")

    text_result = "ACCESS GRANTED." if input_password == password else "ACCESS DENIED."
    print(text_result)
main()
