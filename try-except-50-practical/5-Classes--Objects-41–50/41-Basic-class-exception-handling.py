class Person:
    def display_name(self):
        try:
            print("Name:", self.name)  # mestipon: This may raise AttributeError if 'name' is missing
        except AttributeError:
            print("Error: 'name' attribute is missing.")

p = Person()
p.display_name()
# Output: Error: 'name' attribute is missing.
# The 'name' attribute is missing, so an AttributeError is raised and caught by the except block.
# The code defines a class `Person` with a method `display_name` that attempts to print the `name` attribute.
# If the `name` attribute is not defined, it raises an `AttributeError`, which is caught and handled gracefully.
# This demonstrates basic exception handling in a class method context.
