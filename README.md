# Proyectos: Reto1 y Reto2

Este repositorio contiene dos proyectos desarrollados en Python, diseñados para practicar conceptos fundamentales de programación.

📂 Reto1/
    └── calculadora_promedios.py # Programa para calcular promedios de materias 
📂 Reto2/ 
    └── sistema_inventario.py # Sistema básico de inventario con POO

## Estructura del Repositorio

### Reto1: Calculadora de Promedios
- **Archivo:** `calculadora_promedios.py`
- **Descripción:** Este programa permite ingresar materias y sus calificaciones, calcula el promedio general, identifica materias aprobadas y reprobadas, y muestra la materia con la mejor y peor calificación.
- **Funciones principales:**
  - `ingresar_calificaciones()`: Solicita nombres de materias y calificaciones.
  - `calcular_promedio(calificaciones)`: Calcula el promedio general.
  - `determinar_estado(calificaciones, umbral=5.0)`: Identifica materias aprobadas y reprobadas.
  - `encontrar_extremos(calificaciones)`: Encuentra la mejor y peor calificación.

### Reto2: Sistema de Inventario
- **Archivo:** `sistema_inventario.py`
- **Descripción:** Sistema básico de inventario que utiliza Programación Orientada a Objetos (POO) para gestionar productos y realizar operaciones de inventario.
- **Características principales:**
  - **Clase Producto:** Gestiona productos con atributos como nombre, precio y cantidad. Incluye métodos para actualizar datos y calcular el valor total del producto.
  - **Clase Inventario:** Permite agregar, buscar productos, listar todos los productos y calcular el valor total del inventario.
  - **Menú interactivo:** Ofrece una interfaz para realizar operaciones como agregar productos, buscar por nombre, listar productos y calcular el valor total del inventario.
  - **Manejo de excepciones:** Valida entradas y maneja errores como datos inválidos o productos no encontrados.

## Requisitos
- Python 3.6 o superior.
- No se requieren dependencias externas.

## Ejecución de los Programas

1. **Reto1:**
   - Navega al directorio correspondiente.
   - Ejecuta el archivo con:
     ```bash
     python calculadora_promedios.py
     ```

2. **Reto2:**
   - Navega al directorio correspondiente.
   - Ejecuta el archivo con:
     ```bash
     python sistema_inventario.py
     ```