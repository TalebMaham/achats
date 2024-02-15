from organ.organ import Component

class Logger(Component):
    def __init__(self):
        self.brain = None
        self.total = 0 
        self.etat = {"name" : "Logger"}
        
    def start(self) : 
        self.brain.subscribe(self, "Customer")
        self.brain.subscribe(self, "Transaction")
        self.brain.subscribe(self, "RabbitmqQueue")

    def operation(self):
        # Implémentation spécifique de l'opération pour une transaction
        pass


    def send(self):
        """
        Méthode pour envoyer l'état de la transaction au cerveau.
        """
 
        self.brain.receive(self.etat, "Logger")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        print(f"{etat["name"]} ----> : {etat}")

    def set_brain(self, cerveau):
        self.brain = cerveau
