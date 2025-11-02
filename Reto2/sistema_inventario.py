# FILE: Reto2/sistema_inventario.py

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero.")
        
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero.")
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

    def __str__(self):
        return f"Producto(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"


class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto: Producto):
        if producto.nombre in self.productos:
            raise ValueError(f"El producto '{producto.nombre}' ya existe en el inventario.")
        self.productos[producto.nombre] = producto

    def buscar_producto(self, nombre: str) -> Producto:
        if nombre not in self.productos:
            raise ValueError(f"El producto '{nombre}' no se encuentra en el inventario.")
        return self.productos[nombre]

    def calcular_valor_total_inventario(self) -> float:
        return sum(producto.calcular_valor_total() for producto in self.productos.values())

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


def menu_interactivo():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir producto")
        print("2. Buscar producto")
        print("3. Mostrar inventario")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                producto = Producto(nombre, precio, cantidad)
                inventario.añadir_producto(producto)
                print("Producto añadido exitosamente.")
            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre)
                print("Producto encontrado:", producto)
            elif opcion == "3":
                print("Inventario:")
                inventario.mostrar_inventario()
            elif opcion == "4":
                valor_total = inventario.calcular_valor_total_inventario()
                print(f"El valor total del inventario es: {valor_total}")
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Ha ocurrido un error inesperado:", e)


if __name__ == "__main__":
    menu_interactivo()