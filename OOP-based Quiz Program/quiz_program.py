# === quiz_program.py ===
'''
Here’s the complete OOP-based Quiz Program
(with 20 questions, user login, and result evaluation) as 
you asked. Since input is not supported in this environment, I'll give you a ready-to-run Python script that works in your local system (VS Code, PyCharm, terminal, etc.).

'''
class Question:
    def __init__(self, prompt, options, correct_option):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option

    def ask(self):
        print("\n" + self.prompt)
        for key, value in self.options.items():
            print(f"{key}. {value}")
        user_answer = input("Enter your option (A/B/C/D): ").strip().upper()
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, student_name):
        self.student_name = student_name
        self.score = 0
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        print(f"\nWelcome {self.student_name}, your quiz is starting now...\n")
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}/{len(self.questions)}:")
            if question.ask():
                print("✅ Correct!")
                self.score += 1
            else:
                print("❌ Incorrect.")
        self.show_result()

    def show_result(self):
        print(f"\n=== RESULT ===")
        print(f"You got {self.score} out of {len(self.questions)}")

        if self.score == 20:
            print("🎉 Congratulations! All answers are correct!")
        elif self.score >= 18:
            print("🌟 Excellent!")
        elif self.score >= 15:
            print("👍 Good Job!")
        elif self.score >= 12:
            print("✅ Passed.")
        else:
            print("❌ Failed. Better luck next time.")


def main():
    print("🔐 Student Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username != password:
        print("❌ Login failed! Username and password must match.")
        return

    quiz = Quiz(student_name=username)

    questions_data = [
        ("What is the capital of France?", {'A': 'Berlin', 'B': 'London', 'C': 'Paris', 'D': 'Madrid'}, 'C'),
        ("Which planet is known as the Red Planet?", {'A': 'Earth', 'B': 'Mars', 'C': 'Jupiter', 'D': 'Venus'}, 'B'),
        ("What is the largest ocean?", {'A': 'Indian', 'B': 'Pacific', 'C': 'Arctic', 'D': 'Atlantic'}, 'B'),
        ("Which animal is called King of Jungle?", {'A': 'Tiger', 'B': 'Lion', 'C': 'Elephant', 'D': 'Bear'}, 'B'),
        ("Who invented light bulb?", {'A': 'Newton', 'B': 'Einstein', 'C': 'Edison', 'D': 'Tesla'}, 'C'),
        ("Which language is used for web apps?", {'A': 'Python', 'B': 'Java', 'C': 'HTML', 'D': 'C++'}, 'C'),
        ("Which one is a programming language?", {'A': 'Snake', 'B': 'Python', 'C': 'Elephant', 'D': 'Horse'}, 'B'),
        ("Who is CEO of Tesla?", {'A': 'Tim Cook', 'B': 'Elon Musk', 'C': 'Bill Gates', 'D': 'Jeff Bezos'}, 'B'),
        ("Which is not a programming language?", {'A': 'Java', 'B': 'HTML', 'C': 'Python', 'D': 'Ruby'}, 'B'),
        ("What is 10 + 5?", {'A': '15', 'B': '20', 'C': '25', 'D': '10'}, 'A'),
        ("Which device displays output?", {'A': 'Keyboard', 'B': 'Monitor', 'C': 'Mouse', 'D': 'Scanner'}, 'B'),
        ("What is 5 * 3?", {'A': '10', 'B': '20', 'C': '15', 'D': '30'}, 'C'),
        ("Which company developed Windows?", {'A': 'Apple', 'B': 'Google', 'C': 'Microsoft', 'D': 'IBM'}, 'C'),
        ("Which is not a web browser?", {'A': 'Chrome', 'B': 'Firefox', 'C': 'Google', 'D': 'Safari'}, 'C'),
        ("Which is an email service?", {'A': 'WhatsApp', 'B': 'Gmail', 'C': 'Instagram', 'D': 'Facebook'}, 'B'),
        ("Which is used to style web pages?", {'A': 'HTML', 'B': 'CSS', 'C': 'Python', 'D': 'SQL'}, 'B'),
        ("What is RAM?", {'A': 'Storage', 'B': 'Memory', 'C': 'Processor', 'D': 'Motherboard'}, 'B'),
        ("HTML stands for?", {'A': 'HyperText Markup Language', 'B': 'HyperText Machine Language', 'C': 'HighText Markup Language', 'D': 'None'}, 'A'),
        ("What is used to store data permanently?", {'A': 'RAM', 'B': 'ROM', 'C': 'Cache', 'D': 'Register'}, 'B'),
        ("What is 100 / 25?", {'A': '2', 'B': '3', 'C': '4', 'D': '5'}, 'D'),
    ]

    for qtext, options, answer in questions_data:
        quiz.add_question(Question(qtext, options, answer))

    quiz.start()

if __name__ == "__main__":
    main()
