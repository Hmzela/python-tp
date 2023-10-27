from password_utils import PasswordUtils
from dice_passphrase import DicePassphraseGenerator

def get_user_input(): # Fonction pour obtenir l'entrée de l'utilisateur et gérer les options.
    print("Choisissez une option :")
    print("1. Tester un mot de passe")
    print("2. Générer un mot de passe")
    print("3. Générer une passphrase")
    print("4. Quitter")

    choice = input("Entrez le numéro de l'option choisie (1/2/3/4) : ").strip()

    if choice == "1":
        password_to_test = input("Entrez le mot de passe à tester : ")
        return "test", password_to_test
    elif choice == "2":
        length = int(input("Longueur du mot de passe : "))
        num_lowercase = int(input("Nombre de minuscules : "))
        num_uppercase = int(input("Nombre de majuscules : "))
        num_digits = int(input("Nombre de chiffres : "))
        num_special = int(input("Nombre de caractères spéciaux : "))

        if num_lowercase + num_uppercase + num_digits + num_special > length:
            print("La somme des critères dépasse la longueur du mot de passe. Veuillez réessayer.")
            return get_user_input()  # Demander à l'utilisateur de réessayer

        return "generate_password", length, num_lowercase, num_uppercase, num_digits, num_special
    elif choice == "3":
        num_words = int(input("Nombre de mots dans la passphrase : "))
        return "generate_passphrase", num_words
    elif choice == "4":
        return "quit", None
    else:
        raise ValueError("Choix invalide. Veuillez entrer 1, 2, 3 ou 4.")

def main(): # Fonction principale qui gère le programme.
    while True:
        try:
            choice, *args = get_user_input()

            if choice == "test":
                password_to_test = args[0]
                entropy = PasswordUtils.calculate_entropy(password_to_test)
                strength = PasswordUtils.evaluate_password_strength(password_to_test)
                print(f"Mot de passe testé : {password_to_test}")
                print(f"Entropie : {entropy}")
                print(f"Force : {strength}")
            elif choice == "generate_password":
                length, num_lowercase, num_uppercase, num_digits, num_special = args
                random_password = PasswordUtils.generate_random_password(
                    length, num_lowercase, num_uppercase, num_digits, num_special)
                entropy = PasswordUtils.calculate_entropy(random_password)
                strength = PasswordUtils.evaluate_password_strength(random_password)
                print(f"Mot de passe généré : {random_password}")
                print(f"Entropie : {entropy}")
                print(f"Force : {strength}")
            elif choice == "generate_passphrase":
                num_words = args[0]
                passphrase = DicePassphraseGenerator.generate_passphrase(number_of_words=num_words)
                entropy = PasswordUtils.calculate_entropy(passphrase)
                strength = PasswordUtils.evaluate_password_strength(passphrase)
                print(f"Passphrase générée : {passphrase}")
                print(f"Entropie : {entropy}")
                print(f"Force : {strength}")
            elif choice == "quit":
                print("Merci d'avoir utilisé le programme. Au revoir!")
                break
        except ValueError as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
