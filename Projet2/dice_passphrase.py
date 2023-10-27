import random

class DicePassphraseGenerator: # Classe utilitaire pour la génération de passphrases basée sur des dés.
    @staticmethod
    def generate_passphrase(number_of_words=6, word_list=None): # Génère une passphrase en utilisant une liste de mots (par défaut, une liste de fruits).
        if not word_list:
            word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig",
                         "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange",
                         "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

        if number_of_words <= 0:
            return ""
# Sélectionne de manière aléatoire un nombre spécifié de mots de la liste pour former une passphrase.
        passphrase = ' '.join(random.choice(word_list) for _ in range(number_of_words))
        return passphrase
