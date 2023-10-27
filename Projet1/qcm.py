import random
from question import Question
# Crée une classe QCM pour gérer un quiz à choix multiple.
class QCM:
    def __init__(self): # Initialise la liste des questions et le score du quiz.
        self.questions = []
        self.score = 0

    def add_question(self, question): # Méthode pour ajouter une question au quiz.
        self.questions.append(question)

    def start_quiz(self):  # Méthode pour démarrer le quiz.
        random.shuffle(self.questions)  # Mélange aléatoirement l'ordre des questions dans le quiz.
        for i, question in enumerate(self.questions, 1):
            random.shuffle(question.options)  # Mélange aléatoirement l'ordre des options de réponse pour chaque question.
            print(f"Question {i}: {question.get_question()}\n")
            options = question.get_options()
            for j, option in enumerate(options, 1): # Affiche les options de réponse avec des lettres (a, b, c).
                print(f"{chr(96 + j)}) {option}")
            while True:
                user_answer = input("Réponse (a/b/c) : ").lower()
                if user_answer in ["a", "b", "c"]: # Convertit la réponse de l'utilisateur en un index (0, 1, 2) pour les options.
                    user_option_index = ord(user_answer) - ord("a")
                    question.user_answer = options[user_option_index]
                    if question.user_answer == question.correct_answer: # Incrémente le score si la réponse de l'utilisateur est correcte.
                        self.score += 1
                    break
                else:
                    print("Veuillez répondre avec 'a', 'b' ou 'c'.")

    def show_score(self): # Méthode pour afficher le score du quiz et les corrections.
        print("\nScore final :")
        print(f"Vous avez obtenu {self.score} sur {len(self.questions)} questions.\n")
        print("Correction :")
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question.get_question()}")
            if question.user_answer:
                user_answer = question.user_answer.lower()
                correct_answer = question.correct_answer.lower()
                if user_answer == correct_answer:
                    print(f"Votre réponse : {question.user_answer} (Correcte)")
                else:
                    print(f"Votre réponse : {question.user_answer} (Incorrecte)")
                print(f"Réponse correcte : {question.correct_answer}\n")
