'''Ejercio 5'''
# PASO 1: CONFIGURACIÓN DEL PERSONAJE
print("--- BIENVENIDO A LA ARENA ---")
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# PASO 2: INICIALIZACIÓN DE ESTADÍSTICAS
vida_jugador = 100            # int
vida_enemigo = 100            # int
pociones = 3                  # int
ataque_pesado_base = 15       # int
ataque_enemigo = 12           # int

print("\n=== INICIO DEL COMBATE ===")

# PASO 3: EL CICLO DE COMBATE
while vida_jugador > 0 and vida_enemigo > 0:
    # Mostrar estado de la arena en cada inicio de turno
    # Usamos .2f si la vida del enemigo muta a float por un crítico, o .0f para limpiar la vista
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo:.0f}) | Pociones: {pociones}")
    print("\nElige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    # Validación estricta del menú
    opcion_txt = input("Opción: ")
    while not opcion_txt.isdigit() or opcion_txt not in ["1", "2", "3"]:
        if not opcion_txt.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: Opción fuera de rango (1, 2 o 3).")
        opcion_txt = input("Opción: ")
    
    opcion = int(opcion_txt)
    
    # LÓGICA DE LAS ACCIONES DEL JUGADOR
    if opcion == 1:
        # ACCIÓN A: ATAQUE PESADO
        # Si el enemigo tiene menos de 20 HP se aplica golpe crítico (float)
        if vida_enemigo < 20:
            dano_final = ataque_pesado_base * 1.5  # Muta a float: 22.5
            print(f">> ¡GOLPE CRÍTICO! Multiplicas tu fuerza.")
        else:
            dano_final = float(ataque_pesado_base)
            
        vida_enemigo -= dano_final
        print(f">> ¡Atacaste al enemigo por {dano_final:.1f} puntos de daño!")
        
    elif opcion == 2:
        # ACCIÓN B: RÁFAGA VELOZ
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")
            
    elif opcion == 3:
        # ACCIÓN C: CURAR
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f">> Te has curado. Tu vida actual es {vida_jugador} HP.")
        else:
            print(">> ¡No quedan pociones! Pierdes tu oportunidad táctica.")

    # CONTROL DE SEGURIDAD: ¿EL ENEMIGO MURIÓ EN ESTE TURNO?
    if vida_enemigo <= 0:
        break  # El enemigo fue derrotado, se salta el contraataque de inmediato

    # TURNO DEL ENEMIGO (CONTRAATAQUE AUTOMÁTICO)
    vida_jugador -= ataque_enemigo
    print(f">> ¡El enemigo contra ataca por {ataque_enemigo} puntos!")
    print("=== NUEVO TURNO ===")

# PASO 4: FIN DEL JUEGO
print("\n" + "═"*40)
if vida_jugador > 0:
    print(f"🎉 ¡VICTORIA! {nombre} has ganado la batalla en la arena.")
else:
    print("💀 DERROTA. Has caído en combate ante el enemigo.")
print("═"*40)
