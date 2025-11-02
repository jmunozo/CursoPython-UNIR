# Calculadora de promedios escolares.

def ingresar_calificaciones():
	"""Solicita al usuario materias y calificaciones.

	Retorna dos listas paralelas: materias (list[str]) y calificaciones (list[float]).
	Valida que la calificación sea un número entre 0 y 10.
	"""
	materias = []
	calificaciones = []

	while True:
		nombre = input("Ingrese el nombre de la materia (o ENTER para terminar): ").strip()
		if nombre == "":
			# si el usuario presiona ENTER sin texto, damos por terminado
			break

		# solicitar calificación con validación
		while True:
			entrada = input(f"Calificación para '{nombre}' (0-10): ").strip()
			try:
				nota = float(entrada.replace(',','.'))
			except ValueError:
				print("Entrada no válida. Introduce un número entre 0 y 10.")
				continue
			if 0.0 <= nota <= 10.0:
				break
			else:
				print("La calificación debe estar entre 0 y 10. Intenta de nuevo.")

		materias.append(nombre)
		calificaciones.append(nota)

		# preguntar si desea continuar
		while True:
			cont = input("¿Desea ingresar otra materia? (s/n): ").strip().lower()
			if cont in ('s', 'si', 'y', 'yes'):
				more = True
				break
			if cont in ('n', 'no'):
				more = False
				break
			print("Respuesta no entendida. Responda 's' o 'n'.")

		if not more:
			break

	return materias, calificaciones


def calcular_promedio(calificaciones):
	"""Devuelve el promedio (float) de la lista de calificaciones.
	Si la lista está vacía, devuelve None.
	"""
	if not calificaciones:
		return None
	return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
	"""Devuelve dos listas de índices: aprobados y reprobados según el umbral."""
	aprobados = []
	reprobados = []
	for i, nota in enumerate(calificaciones):
		if nota >= umbral:
			aprobados.append(i)
		else:
			reprobados.append(i)
	return aprobados, reprobados

def encontrar_extremos(calificaciones):
	"""Devuelve una tupla (idx_max, idx_min) con los índices de la nota mayor y menor.
	Si la lista está vacía, devuelve (None, None).
	"""
	if not calificaciones:
		return None, None
	idx_max = max(range(len(calificaciones)), key=lambda i: calificaciones[i])
	idx_min = min(range(len(calificaciones)), key=lambda i: calificaciones[i])
	return idx_max, idx_min


def main():
	print("--- Calculadora de promedios escolares ---")
	materias, calificaciones = ingresar_calificaciones()

	if not materias:
		print("No se ingresaron materias. Saliendo...")
		print("¡Hasta luego!")
		return

	# mostrar todas las materias con sus calificaciones
	print("\nResumen de materias y calificaciones:")
	for i, (m, c) in enumerate(zip(materias, calificaciones), start=1):
		print(f" {i}. {m}: {c:.2f}")

	promedio = calcular_promedio(calificaciones)
	aprobados, reprobados = determinar_estado(calificaciones)
	idx_max, idx_min = encontrar_extremos(calificaciones)

	print(f"\nPromedio general: {promedio:.2f}")

	# materias aprobadas
	if aprobados:
		print("\nMaterias aprobadas:")
		for i in aprobados:
			print(f" - {materias[i]}: {calificaciones[i]:.2f}")
	else:
		print("\nNo hay materias aprobadas.")

	# materias reprobadas
	if reprobados:
		print("\nMaterias reprobadas:")
		for i in reprobados:
			print(f" - {materias[i]}: {calificaciones[i]:.2f}")
	else:
		print("\nNo hay materias reprobadas.")

	# extremos
	if idx_max is not None:
		print(f"\nMejor calificación: {materias[idx_max]} -> {calificaciones[idx_max]:.2f}")
	if idx_min is not None:
		print(f"Peor calificación: {materias[idx_min]} -> {calificaciones[idx_min]:.2f}")

	print("\n¡Gracias por usar la calculadora de promedios!")

if __name__ == "__main__":
	main()