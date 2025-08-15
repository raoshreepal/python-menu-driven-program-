class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            raise ValueError("Cannot divide by zero.") from e  # mestipon: Chaining exceptions

calc = Calculator()
# calc.divide(10, 0)  # Uncomment to test
