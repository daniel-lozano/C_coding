#variables
.PHONY: all

var= ${ARGS} #Define una variable que sera usada a lo largo del make
 
all: open closed

open: 

	python open_boundary.py $(var)

closed: 
	python closed_boundary.py $(var)
	
clean:
	rm *~ *.dat *.png


#Para ejecutar una parte especifica del Makefile en la terminal se escribe el codigo "make <parte especifica>"


#clean es una opcion util para borrar los datos creados por make, de esta forma make puede volver a ser utilizado ya que no habra archivos creados (o actualizados)
