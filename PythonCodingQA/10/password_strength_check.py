def check_password_strength(password):
    if len(password)<8:
        return "Weak"
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password) 
    if has_digit and has_upper and has_lower:
        return "Strong"
    else:
        return "Weak"
print(check_password_strength("Shalu1234"))
print(check_password_strength("password"))
print(check_password_strength("PASSWORD"))
print(check_password_strength("pass12"))