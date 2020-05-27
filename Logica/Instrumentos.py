from abc import ABC, abstractmethod
class Instrumentos(ABC):
	def prepararInstrumento(self,nombre):
		pass
	def tocarInstrumento(self,nombre):
		pass

	
class Violin(Instrumentos):
	def prepararInstrumento(self,nombre):
		imagen="static/violin.jpg"
		violinp="Preparando Violin"
		return nombre,violinp,imagen
	def tocarInstrumento(self,nombre):
		violint=" Tocando Violin"
		return nombre,violint
		
class Guitarra(Instrumentos):
	def prepararInstrumento(self,nombre):
		imagen="static/guitarra.jpg"
		guitarrap=" Preparando Guitarra"
		return nombre,guitarrap,imagen
	def tocarInstrumento(self,nombre):
		guitarrat=" Tocando Guitarra"
		return nombre,guitarrat
		

class Trompeta(Instrumentos):
	def prepararInstrumento(self,nombre):
		imagen="static/trompeta.jpg"
		trompetap=" Preparando Trompeta"
		return nombre,trompetap,imagen
	def tocarInstrumento(self,nombre):
		trompetat=" Tocando Trompeta"
		return nombre,trompetat
		




