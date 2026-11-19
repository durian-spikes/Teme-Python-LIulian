while True:
    password = input("Password: ")

    errors = []

    if len(password) < 8:
        errors.append("Too short (minimum 8).")

    if not any(ch.isupper() for ch in password):
        errors.append("Missing an uppercase letter.")

    if not any(ch.islower() for ch in password):
        errors.append("Missing a lowercase letter.")

    if not any(ch.isdigit() for ch in password):
        errors.append("Missing a digit.")

    if " " in password:
        errors.append("No spaces allowed.")

    # Print all errors
    if errors:
        for error in errors:
            print(error)
    else:
        print("Password accepted.")
        break