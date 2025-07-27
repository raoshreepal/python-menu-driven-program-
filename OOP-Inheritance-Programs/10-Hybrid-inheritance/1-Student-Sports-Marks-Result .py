class Student:
    def __init__(self, name):
        self.name = name

class Marks(Student):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

class Sports:
    def __init__(self, sport_score):
        self.sport_score = sport_score

class Result(Marks, Sports):
    def __init__(self, name, marks, sport_score):
        Marks.__init__(self, name, marks)
        Sports.__init__(self, sport_score)

    def show(self):
        print(f"{self.name} | Marks: {self.marks}, Sports Score: {self.sport_score}")

r = Result("Rohit", 85, 90)
r.show()
