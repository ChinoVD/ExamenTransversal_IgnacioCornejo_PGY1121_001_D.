import numpy as np
from os import system
true: None

escenario = np.array([
    [1,  2,  3,  4,  5,  6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
])

precios = {
    'Platinum, $120.000. (Asientos del 1 al 20)': 120000,
    'Gold, $80.000. (Asientos del 21 al 50)': 80000,
    'Silver, $50.000. (Asientos del 51 al 100)': 50000
}
publico = {}

def clear_screen():
    system("cls")

def obtener_cantidada_entradas():
        while true:
            try:
                cantidad=int(input("Ingrese la cantidad de entradas que desea. (de 1 a 3)"))
                if cantidad < 1 or cantidad > 3:
                    raise ValueError
                return cantidad
            except ValueError:
                print ("Cantidad invalida")

def comprar_asiento():
    clear_screen()
    print("El estado actual de los asientos es:")
    print_asientos(escenario)

    fila = obtener_numero("Ingrese el número de fila: ", 1, escenario.shape[0])
    columna = obtener_numero("Ingrese el número de columna: ", 1, escenario.shape[1])

    if escenario[fila-1, columna-1] == 0:
        print("El asiento no está disponible.")
        return
   
    if escenario[fila-1, columna-1] in publico:
        print("El asiento ya está ocupado.")
        return

    precio = None
    if 1 <= escenario[fila-1, columna-1] <= 20:
        precio = 'Platinum, $120.000. (Asientos del 1 al 20)'

    elif 21 <= escenario[fila-1, columna-1] <= 50:
        precio = 'Gold, $80.000. (Asientos del 21 al 50)'

    elif 51 <= escenario[fila-1, columna-1] <= 100:
        precio = 'Silver, $50.000. (Asientos del 51 al 100)'

    print(f"Precio: ${precios[precio]}")

    publico_rut = obtener_rut("Ingrese el RUN del comprador (sin guiones ni dígito verificador): ")
    if publico_rut is None:
        print("RUN inválido.")
        return

    if len(publico_rut) != 8:
        print("El RUN debe tener 8 dígitos.")
        return

    publico[escenario[fila-1, columna-1]] = {
        'rut': publico_rut,
        'tipo': precio
    }
    escenario[fila-1, columna-1] = 0
    print("Operación realizada correctamente.")

def obtener_numero(mensaje, minimo, maximo):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < minimo or numero > maximo:
                raise ValueError
            return numero
        except ValueError:
            print("Número inválido. Intente nuevamente.")

def obtener_rut(mensaje):
    while True:
        rut = input(mensaje)
        if rut.isdigit():
            return rut
        print("RUN inválido. Intente nuevamente.")

def asientos_disponibles():
    clear_screen()
    print("El estado actual de los asientos es:")
    print_asientos(escenario)

def print_asientos(arr):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] == 0:
                print('X', end='\t')
            else:
                print(arr[i, j], end='\t')
           
            if j % 2 == 1:
                print('\t', end='')

        if i % 2 == 1:
            print()
        print()

def listado_publico():
    clear_screen()
    pasajeros_ordenados = sorted(publico.items(), key=lambda x: x[1]['rut'])
    for asiento, datos in pasajeros_ordenados:
        print(f"Asiento: {asiento}, RUN: {datos['rut']}")

def ganancias_totales():
    clear_screen()
    total_ganancias = 0
    for asiento, datos in publico.items():
        tipo = datos ['tipo']
        cantidad_entradas = len (publico[asiento])
        ganancia = precios [tipo]
        ganancia_total = ganancia *cantidad_entradas
        total_ganancias += ganancia_total
        print (f"Tipo de entrada: {tipo}")
        print (f"Cantidad de entradas:{cantidad_entradas}")
        print (f"Ganancia por entrada: ${ganancia}")
        print (f"Ganancia total: ${ganancia_total}\n")
    print (f"Ganancias totales: ${total_ganancias}")

def menu():
    while True:
        print ("\n--------- Menú -------------------")
        print ("*****Concierto Michael Jam*****")
        print("1. Comprar Entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Listado de clientes")
        print("4. Ganancias totales")
        print("5. Salir")
        print ("------------------------------------")
        print ("By:Creativos.cl")


        opcion = obtener_numero("Seleccione una opción: ", 1, 5)

        if opcion == 1:
            comprar_asiento()
        elif opcion == 2:
            asientos_disponibles()
        elif opcion == 3:
            listado_publico()
        elif opcion == 4:
            ganancias_totales()
        elif opcion == 5:
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def main():
    menu()

if __name__ == "__main__":
    main()
    
    

    