from abc import ABC, abstractmethod
class Instrumentos(ABC):
	def prepararInstrumento(self,nombre):
		pass
	def tocarInstrumento(self,nombre):
		pass

	
class Violin(Instrumentos):
	def prepararInstrumento(self,nombre):
		print(nombre+" Preparando Violin")
	def tocarInstrumento(self,nombre):
		print(nombre+" Tocando Violin")
		
class Guitarra(Instrumentos):
	def prepararInstrumento(self,nombre):
		print(nombre+" Preparando Guitarra")
	def tocarInstrumento(self,nombre):
		print(nombre+" Tocando Guitarra")
		

class Trompeta(Instrumentos):
	def prepararInstrumento(self,nombre):
		print(nombre+" Preparando Trompeta")
	def tocarInstrumento(self,nombre):
		print(nombre+" Tocando Trompeta")
		




