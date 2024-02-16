# -*- coding: utf-8 -*-
from organ.organ import Component

class RabbitmqQueue(Component):
    def __init__(self):
        self.brain = None
        self.etat = []



    def start(self) : 
        self.brain.subscribe(self, "transaction")

    def operation(self):
       
        pass


    def send(self):
       
   
        self.brain.receive(self.etat, "rabbitmq")
      
    def receive(self, etat, name):

        if etat["name"] == "transaction" : 
            print(f"Rabbitmq a reçu {etat}")
            self.etat.append(etat)
            print(etat)



    def set_brain(self, cerveau):
        self.brain = cerveau

    def get(self) :
            return self.etat 