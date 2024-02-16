# -*- coding: utf-8 -*-
from organ.organ import Component

class Machine(Component):
    def __init__(self):
        self.brain = None
        self.etat = {"name" : "machine"}


    def start(self) : 
        self.brain.subscribe(self, "transaction")

    def operation(self):
       
        pass


    def send(self):

        self.brain.receive(self.etat, "machine")

    def receive(self, etat, name):

        if etat["name"] == "transaction" : 
            if  "machine_action" in etat : 
                        print(f"Machine reçoit : {etat["machine_action"]}")
    
            
    def set_brain(self, cerveau):
        self.brain = cerveau

