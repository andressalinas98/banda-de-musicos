from Banda import Banda as bn
import random

class Serenata():

	def __init__(self):
		cantidad=random.randint(1,10)
		bn.crearBanda(cantidad)
		return print("cantidad de miembros: ",cantidad)



