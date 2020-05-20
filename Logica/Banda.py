from Instrumentos import Instrumentos:

class Banda():
	instrumento=Instrumentos():
	InstrumentosList=[Violin(),Guitarra(),Trompeta()]
	def crearBanda(self,cantidad):
		for x in range(cantidad):
			import random
			cantidad2=random.randint(0,2)
			Instrumento=InstrumentosList[cantidad2]
			
			
			