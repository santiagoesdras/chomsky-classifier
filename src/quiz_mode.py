from random import choice, shuffle

class QuizMode:
    def __init__(self, grammar_examples):
        self.grammar_examples = grammar_examples
        self.score = 0
        self.total_questions = 0

    def generate_quiz(self, num_questions=5):
        shuffle(self.grammar_examples)
        return self.grammar_examples[:num_questions]

    def ask_question(self, grammar):
        print(f"Classify the following grammar: {grammar['rules']}")
        user_answer = input("Enter the type (0: Recursively Enumerable, 1: Context-Sensitive, 2: Context-Free, 3: Regular): ")
        correct_answer = grammar['type']
        self.total_questions += 1

        if user_answer == str(correct_answer):
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}")

    def display_results(self):
        print(f"You scored {self.score} out of {self.total_questions}.")

    def run_quiz(self, num_questions=5):
        quiz_questions = self.generate_quiz(num_questions)
        for grammar in quiz_questions:
            self.ask_question(grammar)
        self.display_results()