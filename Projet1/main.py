from qcm import QCM
from question import Question

if __name__ == "__main__":
    # Crée 10 instances de la classe Question pour représenter les questions du QCM.
    question1 = Question("Quelle est la capitale du Japon ?", ["Pékin", "Tokyo", "Séoul"], "Tokyo")
    question2 = Question("Quel est le symbole chimique de l'or ?", ["Go", "Ag", "Au"], "Au")
    question3 = Question("Qui a écrit l'Odyssée ?", ["Homere", "Dante Alighieri", "Virgile"], "Homere")
    question4 = Question("Quel est le plus grand désert du monde ?", ["Le Sahara", "Le désert d'Atacama", "Le désert du Kalahari"], "Le Sahara")
    question5 = Question("Quel est le nom de la plus haute montagne du monde ?", ["Mont Everest", "Mont Kilimandjaro", "Mont McKinley"], "Mont everest")
    question6 = Question("Quel est le gaz le plus abondant dans l'atmosphère de la Terre ?", ["Oxygène", "Azote", "Argon"], "Azote")
    question7 = Question("Qui a peint Les Tournesols ?", ["Claude Monet", "Vincent van Gogh", "Salvador Dalí"], "Vincent van Gogh")
    question8 = Question("Quel est le premier jour de la semaine dans de nombreuses cultures ?", ["Lundi", "Mardi", "Dimanche"], "Dimanche")
    question9 = Question("Quelle est la planète la plus éloignée du soleil dans notre système solaire ?", ["Neptune", "Uranus", "Jupiter"], "Neptune")
    question10 = Question("Qui a écrit 1984 ?", ["George Orwell", "Aldous Huxley", "Ray Bradbury"], "George Orwell")

    qcm = QCM()  # Crée une instance de la classe QCM.
    # Ajoute les questions au QCM en utilisant la méthode add_question.
    qcm.add_question(question1)
    qcm.add_question(question2)
    qcm.add_question(question3)
    qcm.add_question(question4)
    qcm.add_question(question5)
    qcm.add_question(question6)
    qcm.add_question(question7)
    qcm.add_question(question8)
    qcm.add_question(question9)
    qcm.add_question(question10)

    qcm.start_quiz() # Démarre le quiz en appelant la méthode start_quiz du QCM.
    qcm.show_score() # Affiche le score final du quiz en appelant la méthode show_score du QCM.


