from organ.organ import Component

class Cart(Component):
    def __init__(self):
        self.brain = None
        self.total = 0 
        self.etat = {"name" : "cart","payment_type": "cashless"}
        self.etat["id"] = 1 
        self.etat["products"] = {}

        self.etat["total"] = self.calculer_total_produits()
    
    def add_to_cart(self, product_name, price, quantity):
        if product_name not in self.etat["products"]:
            self.etat["products"][product_name] = {"prix": price, "quantite": 0}
        self.etat["products"][product_name]["quantite"] += quantity
        self.total += price * quantity
        self.etat["total"] = self.calculer_total_produits()
        return f"{quantity} {product_name}(s) added to cart."


    def remove_from_cart(self): 
        pass  

    def update_quantity(self) : 
        pass 

    def clear_cart(self) : 
        pass 

    def calculate_total(self) : 
        pass  

    def view_cart(self) : 
        pass  

    def check_product(self) : 
        pass 

    def apply_discount(self) :
        pass 

    def checkout(self) : 
        pass 


    def save_cart(self) : 
        pass 


    def start(self) : 
        self.brain.subscribe(self, "transaction")


    def operation(self):
        # Implémentation spécifique de l'opération pour une transaction
        pass


    def send(self):
        """
        Méthode pour envoyer l'état de la transaction au cerveau.
        """

        self.brain.receive(self.etat, "cart")

    def receive(self, etat, name):
        """
        Méthode pour recevoir l'état d'un autre organe.

        Args:
            etat: Dictionnaire contenant l'état de l'organe émetteur.
        """
        if etat["name"] == "transaction" : 
            if "cart" in etat : 
                if etat["cart"] == "in_progress" : 
                    print(f"Panier a reçu : Demande en cours de traitement")
                if etat["cart"] == "ready" : 
                    self.etat["products"] = {}
                    self.etat["total"] = 0
                    print(f"Cart a reçu : {etat}")
                else : 
                    print(f"Carte a reçu {etat}")




    def calculer_total_produits(self):
            total = 0
            for product in self.etat["products"].values():
                total += product["prix"] * product["quantite"]
            return total

    def set_brain(self, cerveau):
        self.brain = cerveau

    def get(self) :
        return self.etat 