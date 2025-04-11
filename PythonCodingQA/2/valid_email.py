def validate_email(email):
    if '@' and '.' and ('.com' or '.in') in email:
        return True
    else:
        return False


print("\n", validate_email("chellingishalini@gmail.com"))