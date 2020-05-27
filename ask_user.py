#Function to check for the user input
def ask_user(message, type_= str, valid=lambda x: True, invalid_message="Invalid"):
    while True:
        try:
            user_input = type_(input(message))
        except (ValueError, TypeError):
            print("Invalid input")
            continue
        if valid(user_input):
            return user_input
        else:
            print(invalid_message)