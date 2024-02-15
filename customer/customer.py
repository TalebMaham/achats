import time
from organ.organ import Component

class Customer(Component):
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
        # etat = {
        #     "name": "Customer",
        #     "prenom" : "Sidi", 
        #     # Ajoutez d'autres attributs spécifiques de la transaction
        # }
        self.brain.receive(self.etat, "Customer")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if "customer" in etat :
            if etat["customer"]["new"] : 
                print(f"Customer a reçu : {etat["customer"]}")
                etat["customer"]["new"] = False
            self.send()

    def set_brain(self, cerveau):
        self.brain = cerveau

    def set_etat(self, etat) : 
        self.etat = etat 