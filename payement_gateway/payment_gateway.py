import time
from organ.organ import Component

class PaymentGateway(Component):
    def __init__(self):
        self.brain = None
        self.etat = {"name" : "payment_gateway"}

    def operation(self):
        # Implémentation spécifique de l'opération pour une transaction
        pass

    def start(self) : 
        self.brain.subscribe(self, "transaction")


    def send(self):
        """
        Méthode pour envoyer l'état de la transaction au cerveau.
        """

        self.brain.receive(self.etat, "payment_gateway")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
    
        if "payment_gateway" in  etat :
            if etat["payment_gateway"] == "in_progress" : 
                if etat["name"] == "transaction" : 
                    print(f"Paymement gateway reçoit : {etat}")
                    self.etat["isAccepted"] = True
                    self.send() 
            
            

    def set_brain(self, cerveau):
        self.brain = cerveau

    def set_etat(self, etat) : 
        self.etat = etat 
