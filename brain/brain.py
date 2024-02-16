# -*- coding: utf-8 -*-
import time
from organ.organ import Organ
import threading
from copy import deepcopy

class Brain(Organ):
    def __init__(self):
        self.organs = []
        self.abonements = {}

    def add_organ(self, organ):
        self.organs.append(organ)   

    def operation(self):
            
            print("Le cerveau pense...")
            threads = []
            for organ in self.organs:
                thread = threading.Thread(target=organ.operation)
                threads.append(thread)
                thread.start()

            time.sleep(10)


    def subscribe(self, organ, name) : 
        if name in self.abonements : 
            self.abonements[name].append(organ)
        else : 
            self.abonements[name] = [organ]





    def send(self, etat, organ) :
        pass

    def receive(self, etat, name) :
        if name in self.abonements :
            etat_copy = deepcopy(etat) 
            for abonne in self.abonements[name] : 
                abonne.receive(etat_copy, name)



