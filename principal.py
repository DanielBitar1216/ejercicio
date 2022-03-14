import math
def area_cuadrado(lado):
	area=lado**2
	print(f"El area es {area}")

def rhombusArea(d1,d2): 
    area = (d1*d2)/2
    return area
	
def volCilindro(radio, altura):
	volCili = math.pi*(radio**2)*altura
	print(f"El Volumen del Cilindro es {volCili}")


area_cuadrado(6) 
volCilindro(4, 5)
	
