import time
from organ.organ import Component

class Convertor(Component):
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
            "name": "Convertor",
            "isAccepted" : True, 
            # Ajoutez d'autres attributs spécifiques de la transaction
        }
        self.brain.receive(etat, "Convertor")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if "Convertor" in etat :
            print(f"convertor a reçu : {etat["convertor"]}")

    def set_brain(self, cerveau):
        self.brain = cerveau

