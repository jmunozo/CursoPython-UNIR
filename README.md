# Calculadora de Promedios (Curso Python - UNIR)

Este pequeño programa en Python permite ingresar materias y sus calificaciones, calcula el promedio general, identifica materias aprobadas y reprobadas, y muestra la materia con la mejor y peor calificación.

Está diseñado para ser sencillo y fácil de usar. El programa usa programación estructurada

## Qué incluye

- `calculadora_promedios.py`: implementación interactiva que solicita al usuario materias y calificaciones.
- Funciones principales:
  - `ingresar_calificaciones()` — pide nombres de materias y calificaciones.
  - `calcular_promedio(calificaciones)` — devuelve el promedio de las calificacioens ingresadas.
  - `determinar_estado(calificaciones, umbral=5.0)` — devuelve lista de aprobados y reprobados.
  - `encontrar_extremos(calificaciones)` — devuelve lista de la mayor y menor calificación.

## Requisitos

- Python 3.6 o superior.
- No hay dependencias externas.

## Uso (ejecución interactiva)

Abre una terminal (PowerShell en Windows) en la carpeta del proyecto y ejecuta:

```powershell
python calculadora_promedios.py
```

Sigue las instrucciones en pantalla:
- Ingresa el nombre de la materia y presiona ENTER.
- Ingresa la calificación (número entre 0 y 10). Puedes usar coma o punto decimal.
- Responde `s` o `n` cuando se te pregunte si deseas ingresar otra materia.
- Para terminar de ingresar materias, simplemente presiona ENTER en el prompt del nombre.

Al finalizar, se mostrará un resumen con:
- Lista de materias y sus calificaciones.
- Promedio general.
- Materias aprobadas y reprobadas ( calificación >= 5.0 : Aprobado).
- Materia con mejor y peor calificación.

## Notas importantes

- El programa valida que las calificaciones estén entre 0 y 10 y rechaza entradas no numéricas.
- Si no se ingresa ninguna materia, el programa muestra un mensaje y termina.