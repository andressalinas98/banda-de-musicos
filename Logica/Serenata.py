from Banda import Banda as bn
import random

class Serenata():

	def __init__(self):
		cantidad=random.randint(0,10)
		bn.crearBanda(cantidad)
		return print("cantidad miembros: ",cantidad)



