import random
import string
import math

class PasswordUtils: # Classe utilitaire pour la gestion des mots de passe.
    @staticmethod
    def calculate_entropy(password): 
        # Calcule l'entropie d'un mot de passe
        total_characters = len(password)
        if total_characters == 0:
            return 0

        character_set = string.printable
        base = len(character_set)
        entropy = math.log(base, 2) * total_characters
        return entropy

    @staticmethod
    def evaluate_password_strength(password):
        # Évalue la force d'un mot de passe
        entropy = PasswordUtils.calculate_entropy(password)
        if entropy >= 80:
            return "Fort"
        elif entropy >= 60:
            return "Moyen"
        else:
            return "Faible"

    @staticmethod
    def generate_random_password(length, num_lowercase, num_uppercase, num_digits, num_special):
        # Génère un mot de passe aléatoire en fonction des critères donnés
        characters = string.ascii_lowercase * num_lowercase + \
                    string.ascii_uppercase * num_uppercase + \
                    string.digits * num_digits + \
                    string.punctuation * num_special

        if len(characters) < length:
            raise ValueError("Pas assez de caractères pour générer le mot de passe.")
        
        password = ''.join(random.sample(characters, length))
        return password
