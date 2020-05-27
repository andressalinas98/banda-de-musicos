from Instrumentos import *
from random import choice
from random import randint
from flask import Flask, render_template, request
app = Flask(__name__)

class Banda():
	def inicio():
		app.run(debug = True)

	@app.route('/')
	def crearBanda():
		cantidad=3
		Lista=[]
		InstrumentosList=[Violin(),Guitarra(),Trompeta()]
		NombreList=['Maria','Susana','Paula', 'Carlos', 'Alberto', 'Juan', 'Fernanda']
		for x in range(cantidad):
			Musico=choice(NombreList)
			obj=choice(InstrumentosList)
			Lista.append(obj.prepararInstrumento(Musico))
			Lista.append(obj.tocarInstrumento(Musico))
		return render_template('index.html', msg = "Banda de musicos", rows = Lista)

	
			


			

			
