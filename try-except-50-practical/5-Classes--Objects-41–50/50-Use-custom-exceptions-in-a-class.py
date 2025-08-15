class ValidationError(Exception): pass  # mestipon: Custom validation error
class AccessError(Exception): pass      # mestipon: Custom access error

class User:
    def __init__(self, role):
        self.role = role

    def access(self, level):
        if self.role != 'admin':
            raise AccessError("Access denied.")  # mestipon: Access control
        if level < 1:
            raise ValidationError("Invalid level.")  # mestipon: Input validation

u = User("user")
try:
    u.access(0)
except (ValidationError, AccessError) as e:
    print("Error:", e)
