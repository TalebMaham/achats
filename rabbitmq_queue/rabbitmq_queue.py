from organ.organ import Component

class RabbitmqQueue(Component):
    def __init__(self):
        self.brain = None
        self.etat = []



    def start(self) : 
        self.brain.subscribe(self, "transaction")

    def operation(self):
        # Implémentation spécifique de l'opération pour une transaction
        pass


    def send(self):
        """
        Méthode pour envoyer l'état de la transaction au cerveau.
        """
   
        self.brain.receive(self.etat, "rabbitmq")
      
    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if etat["name"] == "transaction" : 
            print(f"Rabbitmq a reçu {etat}")
            self.etat.append(etat)
            print(etat)



    def set_brain(self, cerveau):
        self.brain = cerveau

    def get(self) :
            return self.etat 