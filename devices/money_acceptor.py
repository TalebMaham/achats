from organ.organ import Component


class Monnayeur(Component):
    def __init__(self):
        self.brain = None
        self.etat = {"name" : "Monnayeur"}
    
    def start(self) : 
        self.brain.subscribe(self, "Transaction")
    
    def operation(self):
        # Implémentation spécifique de l'opération pour un Monnayeur
        pass

    def send(self):
        """
        Méthode pour envoyer l'état du Monnayeur au cerveau.
        """
        self.brain.receive(self.etat, "Monnayeur")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if "money_acceptor" in etat : 
            if etat["money_acceptor"]["new"]:
                self.transaction()
                etat["money_acceptor"]["new"] = False
                print(f"Monnayeur a reçu  : {etat["money_acceptor"]}")
                self.send()

    def set_brain(self, cerveau):
        self.brain = cerveau


    def transaction(self) : 
        self.etat["transaction"] = {
                "new" : True, 
                "isAccepted" : True

        }



    def accept_money(self) : 
        pass 

    def return_money(self) : 
        pass  

    def check_acceptance(self) : 
        pass 

    def empty(self) : 
        pass  

    def check_capacity(self) : 
        pass  

    def replenish(self) : 
        pass  


    def check_status(self) :
        pass 


    def maintenance(self) : 
        pass  

    def calibrate(self) : 
        pass  

    def  log_transactions(self) : 
        pass 

