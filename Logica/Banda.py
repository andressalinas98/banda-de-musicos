from Instrumentos import *
from random import choice

class Banda():

	def crearBanda(cantidad):
		InstrumentosList=[Violin(),Guitarra(),Trompeta()]
		NombreList=['Maria','Susana','Paula', 'Carlos', 'Alberto', 'Juan', 'Fernanda']
		for x in range(cantidad):
			#TipoInst=choice(InstrumentosList)
			Musico=choice(NombreList)
			obj=choice(InstrumentosList)
			obj.prepararInstrumento(Musico)
			obj.tocarInstrumento(Musico)

			


			

			
