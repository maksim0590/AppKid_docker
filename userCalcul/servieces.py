
def calcul(a, b, operation):
    if operation == '-':
        c = a - b
        return c
    elif operation == '+':
        c = a + b
        return c
    elif operation == '*':
        c = a * b
        return c
    elif operation == '/':
        c = a / b
        return c

def calculThreeLevel(a, b, f, operation, operatorTwo):
    if operation == '-' and operatorTwo == '-':
        c = a - b - f
        return c
    elif operation == '+' and operatorTwo == '+':
        c = a + b + f
        return c
    elif operation == '-' and operatorTwo == '+':
        c = a - b + f
        return c
    elif operation == '+' and operatorTwo == '-':
        c = a + b - f
        return c

def calculTwoLevel (a, b, operator):
    if operator == '+':
        c = a + b
        return c
    elif operator == '-':
        if a <= b:
            c = b - a
            return c
        elif a > b:
            c = a - b
            return c