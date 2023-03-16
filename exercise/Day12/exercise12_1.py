user_prompt = input("Enter a password: ")


def password_length(password_local):
    if len(password_local) > 8:
        return True
    else:
        return False


def has_numbers(user_password):
    return any(char.isdigit() for char in user_password)


def has_uppercase(user_password):
    return any(char.isupper() for char in user_password)


def strength_of_password(user_password):
    if password_length(user_prompt) and has_uppercase(user_prompt) and has_numbers(user_prompt):
        return "Strong Password"
    else:
        return "Weak Password"


print(strength_of_password(user_prompt))