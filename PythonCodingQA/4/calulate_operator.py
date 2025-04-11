def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "error division"
        else:
            return a/b
    else:
        return "invalid operator"


print(calculator(15, 5, '+'))
