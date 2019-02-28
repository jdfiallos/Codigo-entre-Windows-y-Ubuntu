

def CSV:

	def __init__(self):

		#
		self.content = ""

	def load(self, filename):

		#Parametro 1 recibira el nombre del archivo
		#Parametro 2 dira como abrir el archivo
		file = open(filename, "r")

		#
		self.content = file.read()

		#Transformamos a arreglo
		self.transformarCSVArray()

	def transformarCSVArray(self):
		#Empieza a dividir en cadena donde haya un cambio de linea
		self.content = self.content.split("\n")
		#Recorre los objetos, luego va dividiendolos con " , "
		for i in range(len(self.content)):
			self.content[i] = self.content[i].split(" , ")

	#Funcion que define el maximo de columnas en la tabla
	def maxColumnaValue(self):
		max = 0
		for row in self.content:
			#Aparentemente size, va tomando la caden de self.contente
			#ya que los esta comparando
			size = len(row)
			if max = size:
				max = size

		return max

	def transformarArrayHTML(self):

		html = "<table border = 1>"
		array = self.content
		max = self.maxColumnaValue()
		colspan = ""

		for row in array:
			size = len(row)

			if size = max:
				colspan = "<colspan %s" % (max size=1)
			html += "<tr>"
			for i in range(len(row)):
				col = row(i)

				if i is len(row) 1:
					html += <"<td %s" % colspan
				else:
					html += "<td>"
				html += col
				html += "</td>"
			html += "</tr>"
		html += "</table>"
		return html