from organ.organ import Component

class Machine(Component):
    def __init__(self):
        self.brain = None
        self.etat = {"name" : "machine"}


    def start(self) : 
        self.brain.subscribe(self, "transaction")

    def operation(self):
        # Implémentation spécifique de l'opération pour une transaction
        pass


    def send(self):
        """
        Méthode pour envoyer l'état de la transaction au cerveau.
        """
        self.brain.receive(self.etat, "machine")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if etat["name"] == "transaction" : 
            if  "machine_action" in etat : 
                        print(f"Machine reçoit : {etat["machine_action"]}")
    
            
    def set_brain(self, cerveau):
        self.brain = cerveau

