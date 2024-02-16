# -*- coding: utf-8 -*-
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
       
        pass


    def send(self):
    
 
        self.brain.receive(self.etat, "Logger")

    def receive(self, etat, name):

        print(f"{etat["name"]} ----> : {etat}")

    def set_brain(self, cerveau):
        self.brain = cerveau
