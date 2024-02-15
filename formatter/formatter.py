import time
from organ.organ import Component

class Formatter(Component):
    def __init__(self):
        self.brain = None


    def start(self) : 
        self.brain.subscribe(self, "Transaction")

    def operation(self):
        # Implémentation spécifique de l'opération pour une transaction
        pass


    def send(self):
        """
        Méthode pour envoyer l'état de la transaction au cerveau.
        """
        etat = {
            "name": "Formatter",
            "isAccepted" : True, 
            # Ajoutez d'autres attributs spécifiques de la transaction
        }
        self.brain.receive(etat, "Formatter")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if "formatter" in etat :
            print(f"Formatter a reçu : {etat["formatter"]}")

    def set_brain(self, cerveau):
        self.brain = cerveau

