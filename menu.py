# menu_calculadora.py

# Función para pedir el nombre del producto y el precio unitario
def pedir_producto():
    nombre = input("Ingresa el nombre del producto: ")
    while True:
        try:
            precio = float(input(f"Ingresa el precio unitario de {nombre}: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido para el precio.")
    return nombre, precio

# Función para pedir la cantidad de un producto
def pedir_cantidad(producto):
    while True:
        try:
            cantidad = int(input(f"¿Cuántos {producto} deseas comprar? "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido para la cantidad.")
    return cantidad

# Función para calcular el total por producto
def calcular_total(precio, cantidad):
    return precio * cantidad

# Función para mostrar el resumen de la compra y calcular el total general
def mostrar_resumen(productos):
    total_general = 0
    print("\n=== Resumen de la Compra ===")
    for producto, datos in productos.items():
        total_producto = calcular_total(datos['precio'], datos['cantidad'])
        total_general += total_producto
        print(f"{producto} - Cantidad: {datos['cantidad']} - Total: ${total_producto:.2f}")
    
    print(f"\nTotal General: ${total_general:.2f}")

# Función principal
def main():
    productos = {}  # Diccionario para almacenar los productos, precios y cantidades
    
    while True:
        print("\n=== Menú ===")
        print("1. Agregar un producto")
        print("2. Ver resumen y calcular total")
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            # Pedir nombre del producto y precio
            nombre, precio = pedir_producto()

            # Pedir cantidad
            cantidad = pedir_cantidad(nombre)

            # Almacenar los datos en el diccionario
            productos[nombre] = {'precio': precio, 'cantidad': cantidad}

        elif opcion == "2":
            # Mostrar resumen y calcular el total general
            if productos:
                mostrar_resumen(productos)
            else:
                print("No hay productos en el carrito para mostrar.")
        
        elif opcion == "3":
            print("¡Gracias por usar el sistema de compras!")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 3.")

if __name__ == "__main__":
    main()
