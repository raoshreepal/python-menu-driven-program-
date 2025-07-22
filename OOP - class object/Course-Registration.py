class CourseRegister:
    def __init__(self):
        self.courses = {}  # course_code as key

    def add_course(self, code, name, credits):
        self.courses[code] = {
            "name": name,
            "credits": credits
        }

    def display_courses(self):
        print("\n--- Course List ---")
        for code, details in self.courses.items():
            print(f"Code: {code}, Name: {details['name']}, Credits: {details['credits']}")

# Usage
reg = CourseRegister()
n = int(input("Enter number of courses to register: "))

for _ in range(n):
    code = input("Enter course code: ")
    name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))
    reg.add_course(code, name, credits)

reg.display_courses()
