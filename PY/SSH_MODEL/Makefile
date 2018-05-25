#variables
.PHONY: all #se utiliza este target para que corra todos los comandos que se desean 

var= ${ARGS} #Define una variable que sera usada a lo largo del make
 
all: blocks no_blocks

blocks: open_b closed_b

no_blocks: open closed

open: 
	python open_boundary.py $(var)

closed: 
	python closed_boundary.py $(var)

open_b: 
	python open_boundary_blocks.py $(var)

closed_b: 
	python closed_boundary_blocks.py $(var)



	
clean:
	rm *~ *.dat *.png


#Para ejecutar una parte especifica del Makefile en la terminal se escribe el codigo "make <parte especifica>"


#clean es una opcion util para borrar los datos creados por make, de esta forma make puede volver a ser utilizado ya que no habra archivos creados (o actualizados)
