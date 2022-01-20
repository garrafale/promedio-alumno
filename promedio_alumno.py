from os import system
system ("cls")

"""CONSIGNA
Realizar un programa que solicite:
*El nombre de un alumno.
*La cantidad de calificaciones que se promediarán.
*Calcular el promedio y si el promedio es mayor o igual a 7, el alumno estará aprobado. Sino, reprobado.
*Al final, deberá preguntarle al usuario si desea capturar a otro alumno y el programa se repetirá mientras haya una respuesta diferente de no."""

pregunta="s"

while pregunta.upper() != "N": 
	system("cls")
	nombre=input("Ingrese el nombre del alumno: ")
	apellido=input("Ingrese el apellido del alumno: ")
	cantidad=int(input("¿Cuántas calificaciones tuvo el alumno?: "))

	print()

	suma_notas=0

	for i in range(cantidad):
		nota=int(input("Ingrese la nota del alumno: "))
		suma_notas=nota+suma_notas

	promedio=suma_notas/cantidad

	print()

	if promedio>=7:
		print("El alumno",nombre,apellido,"ha sido aprobado con un promedio de",promedio)

	else:
		print("El alumno",nombre,apellido,"ha sido reprobado con un promedio de",promedio)

	print()

	pregunta=input("¿Quiere saber el promedio de algún otro alumno? (S/N): ")
