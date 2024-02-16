# -*- coding: utf-8 -*-
import time
from organ.organ import Component

class PaymentGateway(Component):
    def __init__(self):
        self.brain = None
        self.etat = {"name" : "payment_gateway"}

    def operation(self):

        pass

    def start(self) : 
        self.brain.subscribe(self, "transaction")


    def send(self):
     
        self.brain.receive(self.etat, "payment_gateway")

    def receive(self, etat, name):
       
    
        if "payment_gateway" in  etat :
            if etat["payment_gateway"] == "in_progress" : 
                if etat["name"] == "transaction" : 
                    print(f"Paymement gateway reçoit : {etat}")
                    self.etat["isAccepted"] = True
                    self.send() 
            
            

    def set_brain(self, cerveau):
        self.brain = cerveau

    def set_etat(self, etat) : 
        self.etat = etat 
