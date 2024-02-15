


# Création des organes
from brain.brain import Brain
from cart.cart import Cart
from customer.customer import Customer
from devices.money_acceptor import Monnayeur
from logger.logger import Logger
from machines.machine import Machine
from payement_gateway.payment_gateway import PaymentGateway
from rabbitmq_queue.rabbitmq_queue import RabbitmqQueue
from stock.stock import Stock
from ticket_printer.ticket_printer import TicketPrinter
from transaction.transaction import Transaction



brain = Brain() 
transaction = Transaction()
cart = Cart()
terminale_gateway = PaymentGateway()
rabbitmq = RabbitmqQueue()
stock = Stock()
machine = Machine()

transaction.set_brain(brain)
cart.set_brain(brain)
terminale_gateway.set_brain(brain)
rabbitmq.set_brain(brain)
stock.set_brain(brain)
machine.set_brain(brain)


brain.add_organ(transaction)
brain.add_organ(cart)
brain.add_organ(terminale_gateway)
brain.add_organ(rabbitmq)
brain.add_organ(stock)
brain.add_organ(machine)


transaction.start()
cart.start()
terminale_gateway.start()
rabbitmq.start()
stock.start()
machine.start()



