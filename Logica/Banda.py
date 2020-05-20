from Instrumentos import Instrumentos
import random

class Banda():

	def crearBanda(cantidad):
		InstrumentosList=['Violin','Guitarra','Trompeta']
		NombreList=['Maria','Susana','Paula', 'Carlos', 'Alberto', 'Juan', 'Fernanda']
		for x in range(cantidad):
			cantidad2=random.randint(0,2)
			cantidad3=random.randint(0,6)
			if (cantidad2%2==1):
				print(Instrumentos.tocarInstrumento(NombreList[cantidad3], InstrumentosList[cantidad2]))
			else:
				print(Instrumentos.prepararInstrumento(NombreList[cantidad3], InstrumentosList[cantidad2]))
