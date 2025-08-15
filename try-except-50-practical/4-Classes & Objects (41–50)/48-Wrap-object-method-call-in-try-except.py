class Division:
    def perform(self, x, y):
        return x / y

d = Division()
try:
    print(d.perform(10, 0))  # mestipon: Division by zero caught here
except ZeroDivisionError as e:
    print("Error during division:", e)
