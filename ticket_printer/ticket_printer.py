from organ.organ import Component

class TicketPrinter(Component):
    def __init__(self):
        self.brain = None
        self.etat = {"name" : "TicketPrinter"}



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
            "name": "TicketPrinter",
            # Ajoutez d'autres attributs spécifiques de la transaction
        }
        self.brain.receive(etat, "TicketPrinter")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if "ticket" in etat : 
                if etat["ticket"]["new"] : 
                    if etat["name"] == "Transaction" : 
                        self.print_transaction(etat)
                    etat["ticket"]["new"] = False

    def set_brain(self, cerveau):
        self.brain = cerveau


    def print_transaction(self, etat) : 
        if "email" in etat["ticket"]["print_type"] : 
            print(f"Ticket email Date :  {etat["date"]} Montant : {etat["amount"]}")
                
        if "papier" in etat["ticket"]["print_type"] : 
            print(f"Ticket papier :  Date : {etat["date"]} Montant : {etat["amount"]}")
                    
    


