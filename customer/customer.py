import time
from organ.organ import Component

class Customer(Component):
    def __init__(self):
        self.brain = None

    def start(self) : 
        self.brain.subscribe(self, "Transaction")
    
    def operation(self):
       
        pass


    def send(self):

  
        self.brain.receive(self.etat, "Customer")

    def receive(self, etat, name):

        if "customer" in etat :
            if etat["customer"]["new"] : 
                print(f"Customer a reçu : {etat["customer"]}")
                etat["customer"]["new"] = False
            self.send()

    def set_brain(self, cerveau):
        self.brain = cerveau

    def set_etat(self, etat) : 
        self.etat = etat 