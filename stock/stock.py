from organ.organ import Component

class Stock(Component):
    def __init__(self):
        self.brain = None
        self.etat = {"name" : "Stock"}
        self.products ={
                "pommes": {"prix": 50, "quantite": 100},
                "bananes": {"prix": 30, "quantite": 150},
                "poires": {"prix": 40, "quantite": 120},
                "oranges": {"prix": 60, "quantite": 80},
                "tomates": {"prix": 80, "quantite": 90},
                "concombres": {"prix": 90, "quantite": 110},
                "salades": {"prix": 100, "quantite": 70},
                "poulet": {"prix": 20, "quantite": 180},
                "boeuf": {"prix": 25, "quantite": 160},
                "saumon": {"prix": 35, "quantite": 140},
                "thon": {"prix": 40, "quantite": 120},
                "crevettes": {"prix": 45, "quantite": 110},
                "oeufs": {"prix": 100, "quantite": 90},
                "lait": {"prix": 80, "quantite": 120},
                "fromage": {"prix": 50, "quantite": 100},
                "yaourts": {"prix": 60, "quantite": 110}
            }






    def operation(self):
        # Implémentation spécifique de l'opération pour une transaction
        pass

    def start(self) : 
        self.brain.subscribe(self, "transaction")

        
    def send(self):
        """
        Méthode pour envoyer l'état de la transaction au cerveau.
        """

        self.brain.receive(self.etat, "Stock")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if etat["name"] == "transaction" : 
            if "stock_decrement" in etat : 
                self.decrement(etat["stock_decrement"])



    def decrement(self, products):
        print(f" Liste de produit reçu par decrement du stock : {products}")
        for product, details in products.items():
            if product in self.products:
                self.products[product]["quantite"] -= details["quantite"]




    def set_brain(self, cerveau):
        self.brain = cerveau

    def get(self) :
        return self.products 