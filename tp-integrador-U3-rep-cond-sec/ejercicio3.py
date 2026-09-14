''' Ejerercicio 3'''
# 1. VALIDACIÓN DEL OPERADOR
operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: El nombre debe contener solo letras.")
    operador = input("Nombre del operador: ")

# Inicialización de la agenda (Variables individuales)
lunes1, lunes2, lunes3, lunes4 = "", "", "", ""
martes1, martes2, martes3 = "", "", ""

# 2. BUCLE PRINCIPAL
while True:
    print("\n--- AGENDA DE TURNOS ---")
    print("1. Reservar turno | 2. Cancelar turno | 3. Ver agenda del día | 4. Ver resumen | 5. Cerrar sistema")
    
    opcion_txt = input("Opción: ")
    if not opcion_txt.isdigit() or int(opcion_txt) < 1 or int(opcion_txt) > 5:
        print("Error: Opción inválida.")
        continue
    opcion = int(opcion_txt)
    
    if opcion == 5:
        print(f"Sistema cerrado por el operador: {operador}.")
        break
        
    # --- COMPROBACIÓN CON RANGE() PARA EL DÍA Y EL PACIENTE ---
    # range(1, 4) abarca las opciones 1, 2 y 3
    if opcion in range(1, 4):
        dia_txt = input("Seleccione el día (1=Lunes, 2=Martes): ")
        while dia_txt not in ["1", "2"]:
            dia_txt = input("Error. Ingrese 1 (Lunes) o 2 (Martes): ")
        dia = int(dia_txt)

    # range(1, 3) abarca únicamente las opciones 1 y 2 (Reservar y Cancelar)
    if opcion in range(1, 3):
        paciente = input("Nombre del paciente: ")
        while not paciente.isalpha():
            paciente = input("Error (solo letras). Nombre del paciente: ")

    # ACCIÓN 1: RESERVAR TURNO
    if opcion == 1:
        if dia == 1:
            if paciente in (lunes1, lunes2, lunes3, lunes4):
                print("Error: El paciente ya tiene un turno este día.")
            elif lunes1 == "": lunes1 = paciente; print("Reservado en Lunes 1.")
            elif lunes2 == "": lunes2 = paciente; print("Reservado en Lunes 2.")
            elif lunes3 == "": lunes3 = paciente; print("Reservado en Lunes 3.")
            elif lunes4 == "": lunes4 = paciente; print("Reservado en Lunes 4.")
            else: print("Error: Lunes sin cupos.")
        else:
            if paciente in (martes1, martes2, martes3):
                print("Error: El paciente ya tiene un turno este día.")
            elif martes1 == "": martes1 = paciente; print("Reservado en Martes 1.")
            elif martes2 == "": martes2 = paciente; print("Reservado en Martes 2.")
            elif martes3 == "": martes3 = paciente; print("Reservado en Martes 3.")
            else: print("Error: Martes sin cupos.")
            
    # ACCIÓN 2: CANCELAR TURNO
    elif opcion == 2:
        encontrado = True
        if dia == 1:
            if lunes1 == paciente: lunes1 = ""
            elif lunes2 == paciente: lunes2 = ""
            elif lunes3 == paciente: lunes3 = ""
            elif lunes4 == paciente: lunes4 = ""
            else: encontrado = False
        else:
            if martes1 == paciente: martes1 = ""
            elif martes2 == paciente: martes2 = ""
            elif martes3 == paciente: martes3 = ""
            else: encontrado = False
            
        print(f"Turno cancelado." if encontrado else "Error: Paciente no encontrado.")

    # ACCIÓN 3: VER AGENDA DEL DÍA
    elif opcion == 3:
        print(f"\n--- AGENDA {'LUNES' if dia == 1 else 'MARTES'} ---")
        if dia == 1:
            print(f"1: {lunes1 or '(libre)'}\n2: {lunes2 or '(libre)'}\n3: {lunes3 or '(libre)'}\n4: {lunes4 or '(libre)'}")
        else:
            print(f"1: {martes1 or '(libre)'}\n2: {martes2 or '(libre)'}\n3: {martes3 or '(libre)'}")


    # ACCIÓN 4: VER RESUMEN GENERAL
    elif opcion == 4:
        ocupados_l = (lunes1!="") + (lunes2!="") + (lunes3!="") + (lunes4!="")
        ocupados_m = (martes1!="") + (martes2!="") + (martes3!="")
        
        if ocupados_l > ocupados_m: mas_demandado = "Lunes"
        elif ocupados_m > ocupados_l: mas_demandado = "Martes"
        else: mas_demandado = "Empate"
            
        print(f"\nLunes -> Ocupados: {ocupados_l} | Libres: {4 - ocupados_l}")
        print(f"Martes -> Ocupados: {ocupados_m} | Libres: {3 - ocupados_m}")
        print(f"Mayor demanda: {mas_demandado}")
