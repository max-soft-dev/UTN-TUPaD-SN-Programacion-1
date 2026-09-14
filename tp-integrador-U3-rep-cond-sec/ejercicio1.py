''' Ejercico 1 '''
# 1. Pedimos y validamos el nombre del cliente
nombre_cliente = input("Cliente: ")
while not nombre_cliente.isalpha():
    print("Error: El nombre debe contener solo letras y no puede estar vacío.")
    nombre_cliente = input("Cliente: ")

# 2. Pedimos y validamos la cantidad de procutos entre (1 y 5)
cantidad_txt = input("Cantidad de productos: ")
while not cantidad_txt.isdigit() or int(cantidad_txt) <= 0 or int(cantidad_txt) > 5:
    print("Error: Ingrese un número entero positivo entre 1 y 5.")
    cantidad_txt = input("Cantidad de productos: ")

cantidad_productos = int(cantidad_txt)

# Inicializamos los acumuladores para los cálculos finales
total_sin_descuento = 0
total_con_descuento = 0.0

# 3. PROCESAR CADA PRODUCTO
for i in range(1, cantidad_productos + 1):
    # Validar el precio del producto actual
    precio_txt = input(f"Producto {i} - Precio: ")
    while not precio_txt.isdigit():
        print("Error: El precio debe ser un número entero.")
        precio_txt = input(f"Producto {i} - Precio: ")
    
    precio_actual = int(precio_txt)
    total_sin_descuento += precio_actual
    
    # Validar la respuesta del descuento (S/N)
    descuento_opcion = input("Descuento (S/N): ").lower()
    while descuento_opcion != 's' and descuento_opcion != 'n':
        print("Error: Ingrese únicamente 'S' o 'N'.")
        descuento_opcion = input("Descuento (S/N): ").lower()
    
    # Aplicar el descuento si corresponde
    if descuento_opcion == 's':
        total_con_descuento += precio_actual * 0.90
    else:
        total_con_descuento += precio_actual

# 4. CÁLCULOS FINALES
ahorro_total = total_sin_descuento - total_con_descuento
promedio_producto = total_con_descuento / cantidad_productos

# Resultados finales
print("\n--- RESUMEN DE COMPRA ---")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_producto:.2f}")


