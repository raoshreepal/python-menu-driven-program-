
'''
8 Admin + Operator + AccessLevel = AdminUser

'''




class User:
    def __init__(self, username):
        self.username = username

class Admin(User):
    def __init__(self, username, admin_code):
        super().__init__(username)
        self.admin_code = admin_code

class Operator(User):
    def __init__(self, username, operator_code):
        super().__init__(username)
        self.operator_code = operator_code

class AccessLevel:
    def __init__(self, level):
        self.level = level

class AdminUser(Admin, Operator, AccessLevel):
    def __init__(self, username, admin_code, operator_code, level):
        Admin.__init__(self, username, admin_code)
        Operator.__init__(self, username, operator_code)
        AccessLevel.__init__(self, level)

    def display(self):
        print(f"User: {self.username} | Admin: {self.admin_code}, Operator: {self.operator_code}, Access: {self.level}")

a = AdminUser("neha_admin", "AD123", "OP456", "Full")
a.display()
