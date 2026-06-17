import csv
import datetime

#Nombre del archivo que utilizare como Base de Datos
archivo_csv = "empleados.csv"


#Funcion para cargar empleados

def cargar_empleados():
    empleados = {}
    try:
        with open(archivo_csv, mode = "r", encoding = "utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    legajo = int(fila["legajo"])
                    empleados[legajo] = {
                        "nombre": fila["nombre"],
                        "sector": fila["sector"],
                        "dias_disponibles": int(fila["dias_disponibles"])
                    }
    except FileNotFoundError:
        print(f"Error critico: No se encontro el archivo {archivo_csv} .")
    return empleados


#Funcion para actualiza el archivo CSV con los datos de los empleados
def actualizar_csv(empleados):
    with open(archivo_csv, mode = "w",newline='', encoding = "utf-8") as archivo:
        campos = ['legajo', 'nombre', 'sector', 'dias_disponibles']
        escritor = csv.DictWriter(archivo, fieldnames = campos)
        escritor.writeheader()
        for legajo, datos in empleados.items():
            escritor.writerow({
                "legajo": legajo,
                "nombre": datos["nombre"],
                "sector": datos["sector"],
                "dias_disponibles": datos["dias_disponibles"]
            })

#Funcion para simular el chatbot
def simular_chatbot():
    #CARGA INICIAL: Leemos el archivo CSV antes de arrancar
    diccionario_empleados = cargar_empleados()
    
    if not diccionario_empleados or len(diccionario_empleados) == 0:
        print("Error no se pudo iniciar el bot porque la base de datos esta vacia o no existe.")
        return

    #INICIALIZACIÓN DE VARIABLES
    estado_actual = "ESPERANDO_LEGAJO"
    legajo_activo = None
    dias_solicitados = None

    print("¡Hola! Bienvenido al asistente virtual de RRHH de FO-NET S.A.")
    print("Por favor, ingresa tu numero de legajo corporativo para iniciar la gestion:")
    print("-" * 70)

    #BUCLE PRINCIPAL DE CONVERSACIÓN
    while estado_actual != "FIN":
        # SOLICITUD DE ENTRADA: Pedimos un dato NUEVO en cada vuelta del bucle
        entrada = input("Empleado: ").strip()

        # =====================================================================
        # ESTADO: ESPERANDO LEGAJO
        # =====================================================================
        if estado_actual == "ESPERANDO_LEGAJO":
            try:
                legajo = int(entrada)
            except ValueError:
                print("Error el legajo debe ser un numero entero (Ej: 1001). Intentalo de nuevo:")
                print("-" * 70)
                continue

            if legajo not in diccionario_empleados:
                print(f"Error el legajo {legajo} no pertenece a FO-NET S.A. Ingresalo nuevamente:")
                print("-" * 70)
                continue

            # Si todo esta bien, guardamos datos y cambiamos de estado
            legajo_activo = legajo
            empleado = diccionario_empleados[legajo]
            print(f"Hola {empleado['nombre']} (Sector: {empleado['sector']}).")
            print(f"Dispones de un saldo de {empleado['dias_disponibles']} dias de vacaciones.")
            print("\n¿Cuantos dias deseas solicitar?")
            print("-" * 70)
            estado_actual = "ESPERANDO_DIAS"

        # =====================================================================
        # ESTADO: ESPERANDO DiAS
        # =====================================================================
        elif estado_actual == "ESPERANDO_DIAS":
            try:
                dias = int(entrada)
                if dias <= 0:
                    raise ValueError
            except ValueError:
                print("Error por favor, ingresa una cantidad de dias valida (mayor a 0):")
                print("-" * 70)
                continue

            saldo_actual = diccionario_empleados[legajo_activo]["dias_disponibles"]
            if dias > saldo_actual:
                print(f"Error saldo insuficiente (Tenes {saldo_actual} dias).")
                print("Proceso finalizado. ¡Hasta luego!")
                print("-" * 70)
                estado_actual = 'FIN'
                break

            # Si el saldo alcanza, guardamos los días y cambiamos de estado
            dias_solicitados = dias
            print("Excelente. Ahora indica la fecha de inicio (Formato DD/MM/AAAA):")
            print("-" * 70)
            estado_actual = "ESPERANDO_FECHA"

        # =====================================================================
        # ESTADO: ESPERANDO FECHA
        # =====================================================================
        elif estado_actual == "ESPERANDO_FECHA":
            try:
                fecha_validada = datetime.datetime.strptime(entrada,"%d/%m/%Y").date()
            except ValueError:
                print("Error formato invalido. Usa el formato DD/MM/AAAA (Ej: 15/10/2026):")
                print("-" * 70)
                continue

            # IMPACTO EN LA BASE DE DATO SIMULADA
            empleado = diccionario_empleados[legajo_activo]
            empleado["dias_disponibles"] -= dias_solicitados
            
            # Guardamos de forma segura en el archivo externo
            actualizar_csv(diccionario_empleados)

            print(f"\n[SOLICITUD PROCESADA CON EXITO]")
            print(f" • Empleado: {empleado['nombre']}")
            print(f" • Dias Otorgados: {dias_solicitados}")
            print(f" • Periodo: A partir del {fecha_validada.strftime('%d/%m/%Y')}")
            print(f" • Nuevo Saldo en CSV: {empleado['dias_disponibles']} dias.")
            print("\nEl estado de tu tramite es: APROBADO AUTOMATICAMENTE.")
            print("-" * 70)
            estado_actual = 'FIN'



if __name__ == "__main__":
    simular_chatbot()