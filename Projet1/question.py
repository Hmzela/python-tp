class Question: # Crée une classe Question pour représenter une question dans un quiz à choix multiple.
    def __init__(self, question, options, correct_answer): # Le constructeur de la classe prend trois arguments : question, options et correct_answer.
        self.question = question # Stocke la question.
        self.options = options # Stocke les options de réponse sous forme de liste.
        self.correct_answer = correct_answer # Stocke la réponse correcte.
        self.user_answer = None # Initialise la réponse de l'utilisateur à None.

    def is_correct(self): # Méthode pour vérifier si la réponse de l'utilisateur est correcte.
        return self.user_answer and self.user_answer.lower() == self.correct_answer # Vérifie si la réponse de l'utilisateur existe (n'est pas None) et si elle correspond à la réponse correcte (insensible à la casse).

    def get_question(self):  # Méthode pour obtenir la question.
        return self.question

    def get_options(self):  # Méthode pour obtenir les options de réponse.
        return self.options