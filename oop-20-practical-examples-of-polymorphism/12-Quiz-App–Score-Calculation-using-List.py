class MCQ:
    def get_score(self, correct):
        return 4 if correct else 0

class TrueFalse:
    def get_score(self, correct):
        return 2 if correct else 0

questions = [MCQ(), TrueFalse(), MCQ()]
answers = [True, False, True]

total = 0
for q, ans in zip(questions, answers):
    total += q.get_score(ans)

print(f"Total Score: {total}")
