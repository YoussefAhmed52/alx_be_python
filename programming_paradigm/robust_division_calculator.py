def safe_divide(numerator, denominator) :
    try:
        num1 = int(numerator)
        num2 = int(denominator)
        result = num1 / num2
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Please enter numeric values only"