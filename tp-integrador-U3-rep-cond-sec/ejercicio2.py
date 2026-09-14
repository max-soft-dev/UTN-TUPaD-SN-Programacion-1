''' Ejercico 2 '''
# CREDENCIALES FIJAS
usuario_correcto = "alumno"
clave_correcta = "python123"

# VARIABLES DE CONTROL DE ACCESO
intentos = 1
ingreso_exitoso = False

# FASE 1: LOGIN (MÁXIMO 3 INTENTOS)
while intentos <= 3:
    print(f"Intento {intentos}/3")
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave: ")
    
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido.")
        ingreso_exitoso = True
        break
    else:
        print("Error: credenciales inválidas.\n")
        intentos += 1

# Si se agotaron los intentos y no logró ingresar
if not ingreso_exitoso:
    print("Cuenta bloqueada.")
    # Terminamos la ejecución del programa aquí si falló el login
    exit()

# FASE 2: MENÚ DE ACCIONES CAMPUS

while True:
    print("\n--- MENÚ DEL CAMPUS ---")
    print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
    opcion_txt = input("Opción: ")
    
    # Validación estricta de entrada numérica
    if not opcion_txt.isdigit():
        print("Error: ingrese un número válido.")
        continue
        
    opcion = int(opcion_txt)
    
    # Validar que esté en el rango correcto
    if opcion < 1 or opcion > 4:
        print("Error: opción fuera de rango.")
        continue

    # EJECUCIÓN DE OPCIONES VALIDADAS
    if opcion == 1:
        print("Estado: Inscripto")
        
    elif opcion == 2:
        nueva_clave = input("Nueva clave: ")
        
        # Validación de longitud mínima (mínimo 6 caracteres)
        if len(nueva_clave) < 6:
            print("Error: mínimo 6 caracteres.")
        else:
            confirmacion = input("Confirme nueva clave: ")
            if nueva_clave == confirmacion:
                clave_correcta = nueva_clave
                print("Clave cambiada con éxito.")
            else:
                print("Error: las claves no coinciden.")
                
    elif opcion == 3:
        print("Mensaje motivacional: 'El éxito es la suma de pequeños esfuerzos repetidos día tras día.'")
        
    elif opcion == 4:
        print("Saliendo del sistema. ¡Hasta luego!")
        break