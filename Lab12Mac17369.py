#Kevin Macario 17369
#Lab 12
import Metodos

print ("Ingresar valores enteros durante use el programa")
numero = 1
while numero != 6:
    print("Seleccione el ejercicio que deseee: (de 1 a 5)")
    print("Ingrese 6 para salir")
    numero = input("Ingrese numero")
    try:
        numero = int(numero)
        if numero == 1:
            Costo = int(input("Costo: "))
            Metodos.ejercicioA(Costo)
        elif numero == 2:
            ram = int(input("RAM: "))
            velocidad = int(input("velocidad: "))
            disco = int(input("disco: "))
            Metodos.ejercicioB(velocidad,ram,disco)
        elif numero == 3:
            presupuesto = int(input("Presupuesto max: "))
            velocidad = int(input("velocidad minima: "))
            color = raw_input("imprimir a color? s O n: ")
            Metodos.ejercicioC(presupuesto, velocidad, color)
        elif numero == 4:
            Model = int(input("ModelO: "))
            velocidad = int(input("velocidad: "))
            RAM = int(input("RAM: "))
            disco = int(input("disco: "))
            Costo = int(input("Costo: "))
            Metodos.ejercicioD(Model, velocidad, RAM, disco, Costo)
        elif numero == 5:
            Costo = int(input("Costo: "))
            Metodos.ejercicioE(Costo)
        else: 
            print("NUMERO INVALIDO")
    except ValueError:
        print("NUMERO INVALIDO")
        print("FIN")
