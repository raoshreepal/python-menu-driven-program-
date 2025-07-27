'''
Person
   ↓
Learner
   ↓
SchoolStudent
   ↓
CollegeStudent
   ↓
UniversityStudent
   ↓
PhDStudent



'''
class Person:
    def __init__(self, name):
        self.name = name

    def identity(self):
        print(f"Name: {self.name}")


class Learner(Person):
    def __init__(self, name, learning_type):
        super().__init__(name)
        self.learning_type = learning_type

    def show_learning_type(self):
        print(f"Learner Type: {self.learning_type}")


class SchoolStudent(Learner):
    def __init__(self, name, learning_type, school_name):
        super().__init__(name, learning_type)
        self.school_name = school_name

    def school_info(self):
        print(f"School: {self.school_name}")


class CollegeStudent(SchoolStudent):
    def __init__(self, name, learning_type, school_name, college_name):
        super().__init__(name, learning_type, school_name)
        self.college_name = college_name

    def college_info(self):
        print(f"College: {self.college_name}")


class UniversityStudent(CollegeStudent):
    def __init__(self, name, learning_type, school_name, college_name, university):
        super().__init__(name, learning_type, school_name, college_name)
        self.university = university

    def university_info(self):
        print(f"University: {self.university}")


class PhDStudent(UniversityStudent):
    def __init__(self, name, learning_type, school_name, college_name, university, research_topic):
        super().__init__(name, learning_type, school_name, college_name, university)
        self.research_topic = research_topic

    def phd_info(self):
        self.identity()
        self.show_learning_type()
        self.school_info()
        self.college_info()
        self.university_info()
        print(f"Ph.D Research Topic: {self.research_topic}")
print("\n--- PhD Student Full Info ---")
phd = PhDStudent(
    name="Aditi Mehra",
    learning_type="Full-Time",
    school_name="Delhi Public School",
    college_name="St. Xavier's College",
    university="Delhi University",
    research_topic="Artificial Intelligence in Education"
)

phd.phd_info()
