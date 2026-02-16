class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self._nombre: str = ""
        self._precio: float = 0.0
        self._cantidad: int = 0
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = float(valor)

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = valor

    def actualizar_precio(self, nuevo_precio: float) -> str:
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = float(nuevo_precio)
        return f"Precio de '{self.nombre}' actualizado a ${self._precio:.2f}"

    def actualizar_cantidad(self, nueva_cantidad: int) -> str:
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad
        return f"Cantidad de '{self.nombre}' actualizada a {self._cantidad} unidades"

    def calcular_valor_total(self) -> float:
        return self._precio * self._cantidad

    def __str__(self) -> str:
        return (
            f"Producto: {self.nombre}\n"
            f"  Precio unitario: ${self._precio:.2f}\n"
            f"  Cantidad: {self._cantidad}\n"
            f"  Valor total: ${self.calcular_valor_total():.2f}"
        )


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto) -> str:
        for p in self.productos:
            if p.nombre.lower() == producto.nombre.lower():
                raise ValueError(
                    f"Ya existe un producto con el nombre '{producto.nombre}'"
                )

        self.productos.append(producto)
        return f"Producto '{producto.nombre}' agregado al inventario"

    def buscar_producto(self, nombre: str) -> Producto | None:
        if nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")

        nombre_buscar = nombre.strip().lower()
        for producto in self.productos:
            if producto.nombre.lower() == nombre_buscar:
                return producto
        return None

    def calcular_valor_inventario(self) -> float:
        total = 0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        return total

    def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío")
            return

        print("\n" + "=" * 50)
        print("LISTADO DE PRODUCTOS EN EL INVENTARIO")
        print("=" * 50)
        for i, producto in enumerate(self.productos, 1):
            print(f"\n--- Producto #{i} ---")
            print(producto)
        print("\n" + "=" * 50)


def obtener_float(mensaje: str) -> float:
    while True:
        try:
            valor = input(mensaje)
            return float(valor)
        except ValueError:
            print("Error: Debe ingresar un número válido")


def obtener_int(mensaje: str) -> int:
    while True:
        try:
            valor = input(mensaje)
            return int(valor)
        except ValueError:
            print("Error: Debe ingresar un número entero válido")


def menu_principal():
    inventario = Inventario()

    while True:
        print("\n" + "=" * 50)
        print("        SISTEMA DE INVENTARIO")
        print("=" * 50)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        print("=" * 50)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- AGREGAR PRODUCTO ---")
            nombre = input("Ingrese el nombre del producto: ")
            precio = obtener_float("Ingrese el precio del producto: ")
            cantidad = obtener_int("Ingrese la cantidad: ")

            try:
                producto = Producto(nombre, precio, cantidad)
                mensaje = inventario.agregar_producto(producto)
                print(f"\n✓ {mensaje}")
            except (ValueError, TypeError) as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "2":
            print("\n--- BUSCAR PRODUCTO ---")
            nombre = input("Ingrese el nombre del producto a buscar: ")

            try:
                producto = inventario.buscar_producto(nombre)
                if producto:
                    print("\n--- PRODUCTO ENCONTRADO ---")
                    print(producto)
                else:
                    print(f"\n✗ No se encontró el producto '{nombre}'")
            except (ValueError, TypeError) as e:
                print(f"\n✗ Error: {e}")

        elif opcion == "3":
            print("\n--- LISTAR PRODUCTOS ---")
            inventario.listar_productos()

        elif opcion == "4":
            print("\n--- VALOR TOTAL DEL INVENTARIO ---")
            total = inventario.calcular_valor_inventario()
            print(f"\nEl valor total del inventario es: ${total:.2f}")
            print(f"Total de productos: {len(inventario.productos)}")

        elif opcion == "5":
            print("\n¡Gracias por usar el sistema de inventario!")
            break

        else:
            print("\n✗ Opción inválida. Por favor seleccione una opción válida.")


if __name__ == "__main__":
    menu_principal()
