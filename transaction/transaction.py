from datetime import datetime
import time
from organ.organ import Component

class Transaction(Component):
    def __init__(self):
        self.brain = None
        self.amount = 50  # Montant de la transaction

        self.date = None  # Date de la transaction
        self.etat = {"name": "transaction"}
        self.etat_cart = {}

    def start(self):
        self.brain.subscribe(self, "cart")
        self.brain.subscribe(self, "payment_gateway")

    def operation(self, etat):
        pass

    def send(self):
        """
        Méthode pour envoyer l'état de la transaction au cerveau.
        """
        self.date = datetime.now()  # Mettre à jour la date
        self.etat["date"] = self.date.strftime("%Y-%m-%d %H:%M:%S")  # Ajouter la date à l'état
        self.brain.receive(self.etat, "transaction")

  
    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if etat["name"] == "cart":
            self.etat["amount"] = etat["total"]
            self.etat["cart"] = "in_progress"
            print(f"L'etat reçu par la transaction {etat}")
            if "payment_type" in etat : 
                if etat["payment_type"] == "cashless" : 
                    self.etat["payment_gateway"] = "in_progress"
                elif etat["payment_type"] == "cash" :
                    self.etat["money_acceptor"] = "in_progress"
                else :
                    self.etat["erreurs"] = "Error : type de payment inconnu"
                    self.etat["result"] = "Transaction not accepted"
                    self.etat["cart"] = f"{self.etat["erreurs"]} {self.etat["result"]}"
            else :
                self.etat["erreurs"] = "Error : type de payment non precisé"
                self.etat["result"] = "Transaction not accepted"
                self.etat["cart"] = f"{self.etat["erreurs"]} {self.etat["result"]}"
            self.etat_cart = etat
            self.send()
        if etat["name"] == "payment_gateway":
            time.sleep(3)
            print(f"Transaction a reçu {etat}")
            self.etat["payment_gateway"] = "passed"
            if etat['isAccepted'] : 
                self.etat["result"] = "Transaction accepted"
                self.etat["stock_decrement"] =  self.etat_cart["products"]
                self.etat["machine_action"] =  f"dispensation des produits {self.etat_cart["products"]}"
            else : 
                self.etat["result"] = "Transaction not accepted"
            self.etat["cart"] = "ready"
            self.etat["erreurs"] = ""
            self.send()

    def set_brain(self, cerveau):
        self.brain = cerveau

    def set_etat(self, etat):
        self.etat = etat

    def get(self) :
        return self.etat 