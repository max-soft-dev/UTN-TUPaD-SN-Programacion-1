''' Ejercicio 4'''
# VALIDACIÓN INICIAL DEL AGENTE
nombre_agente = input("Ingrese el nombre del agente: ")
while not nombre_agente.isalpha():
    print("Error: El nombre debe contener solo letras.")
    nombre_agente = input("Ingrese el nombre del agente: ")

# VARIABLES INICIALES DEL JUEGO
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

# Contador para la regla anti-spam
forzar_seguidas = 0

print(f"\n¡Bienvenido Agente {nombre_agente} a la Bóveda!")

# BUCLE PRINCIPAL DEL JUEGO
# El juego continúa mientras queden recursos, falten cerraduras
# y NO se cumpla la condición de bloqueo por alarma (alarma activa con tiempo <= 3)
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    
    # Mostrar estado actual en cada turno
    print("\n" + "="*30)
    print(f"ESTADO DE LA MISIÓN:")
    print(f"Energía: {energia}% | Tiempo restante: {tiempo}h")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVA 🚨' if alarma else 'APAGADA 🟢'}")
    print(f"Código parcial de hackeo: [{codigo_parcial}]")
    print("="*30)
    
    # Mostrar Menú
    print("1. Forzar cerradura (Costo: -20 energía, -2 tiempo)")
    print("2. Hackear panel (Costo: -10 energía, -3 tiempo)")
    print("3. Descansar (Costo: +15 energía, -1 tiempo)")
    
    opcion_txt = input("Seleccione su acción (1-3): ")
    while opcion_txt not in ["1", "2", "3"]:
        print("Error: Ingrese una opción válida (1, 2 o 3).")
        opcion_txt = input("Seleccione su acción (1-3): ")
    
    opcion = int(opcion_txt)
    
    # ACCIÓN 1: FORZAR CERRADURA
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1  # Aumenta la racha de spam
        
        # Evaluación de la Regla Anti-Spam
        if forzar_seguidas == 3:
            print("\n⚠️ ¡La cerradura se trabó por intentar forzar repetidamente! La alarma se ha activado.")
            alarma = True
            # Al ser el tercer intento fallido por spam, no abre la cerradura
            
        else:
            # Si no se trabó por spam, evaluamos riesgo de alarma por baja energía
            if energia < 40:
                print("\n⚠️ Alerta: Tu energía es baja. Hay riesgo de activar la alarma.")
                numero_riesgo = input("Para mantener el sigilo, elija un número entre 1 y 3: ")
                while numero_riesgo not in ["1", "2", "3"]:
                    numero_riesgo = input("Error. Elija un número entre 1 y 3: ")
                
                if int(numero_riesgo) == 3:
                    print("¡Hiciste demasiado ruido! Alarma activada.")
                    alarma = True
            
            # Si superó los filtros o la alarma ya estaba activa pero no fue por spam, abre cerradura
            if forzar_seguidas < 3:
                cerraduras_abiertas += 1
                print("\n🔓 ¡Éxito! Lograste forzar y abrir una cerradura.")

    # ACCIÓN 2: HACKEAR PANEL
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0  # Rompe la racha de spam
        
        print("\n💻 Iniciando protocolo de hackeo...")
        for paso in range(1, 5):
            print(f" -> Procesando nodo {paso}/4...")
            codigo_parcial += "A"  # Suma una letra al código parcial
            
        print(f"Progreso guardado. Código actual: {codigo_parcial}")
        
        # Validar si el código completó la longitud requerida
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("⚡ ¡Código descifrado! Una cerradura se abrió automáticamente.")
                # Opcional: Podríamos reiniciar el código parcial si quisiéramos usarlo de nuevo,
                # pero el enunciado no lo pide, así que acumula.

    # ACCIÓN 3: DESCANSAR
    elif opcion == 3:
        tiempo -= 1
        forzar_seguidas = 0  # Rompe la racha de spam
        
        # Penalización si la alarma está encendida
        if alarma:
            print("\n🔊 El sonido de la alarma no te deja descansar bien.")
            energia -= 10
        
        # Recuperación de energía limitando el máximo a 100 de forma matemática
        energia_antes = energia
        energia = min(100, energia + 15)
        print(f"\n💤 Descansaste. Energía recuperada: +{energia - energia_antes}%.")

# EVALUACIÓN DE CONDICIONES DE FIN DE JUEGO
print("\n" + "#"*40)
if cerraduras_abiertas == 3:
    print(f"🎉 ¡VICTORIA! El agente {nombre_agente} abrió la bóveda y escapó con el botín.")
elif alarma and tiempo <= 3:
    print(f"🚨 DERROTA: El sistema detectó la intrusión con la alarma activa y bloqueó la bóveda por completo.")
elif energia <= 0:
    print(f"💀 DERROTA: El agente {nombre_agente} se desmayó por falta de energía dentro de la instalación.")
elif tiempo <= 0:
    print(f"⏱️ DERROTA: Se agotó el tiempo de la misión. Las fuerzas de seguridad capturaron al agente.")
print("#"*40)
