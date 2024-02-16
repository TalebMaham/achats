import time
from organ.organ import Component

class Formatter(Component):
    def __init__(self):
        self.brain = None


    def start(self) : 
        self.brain.subscribe(self, "Transaction")

    def operation(self):
       
        pass


    def send(self):
  
        self.brain.receive(self.etat, "Formatter")

    def receive(self, etat, name):
   
        if "formatter" in etat :
            print(f"Formatter a reçu : {etat["formatter"]}")

    def set_brain(self, cerveau):
        self.brain = cerveau

