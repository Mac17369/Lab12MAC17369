#Kevin Macario 17369
#Lab 12

#################
#Ejercicio 1
#################
def ejercicioA(costo):
    if costo >= 0:
        try:
            costo = int(costo)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=macario1270")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
				#QUERY 1
                cursor.execute('''
                            SELECT pc.model, pc.speed, pc.ram, pc.hd, pc.price
                            FROM pc
                            ORDER BY (ABS(%s - pc.price)) ASC LIMIT 1;''', (costo,))
                #Se guarda el resultado
                result = cursor.fetchall()
                for i in result:
                    print (i)
                print("")
                conexion.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error durante la transaccion")
            finally:
                cursor.close()
                conexion.close()
                print("Fin")
                pass
            pass
        except ValueError:
            print("Ingrese un numero")
    else:
        print("Ingrese un costo valido (mayor a 0)")

#################
#Ejercicio 2
#################
def ejercicioB(vel, ram, disco):
    if vel > 0 and ram > 0 and disco > 0:
        try:
            vel = int(vel)
            ram = int(ram)
            disco = int(disco)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=macario1270")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT product.fabricante, laptop.model, laptop.speed, laptop.ram, laptop.hd, laptop.screen, laptop.price
                            FROM laptop
                                JOIN product ON product.model = laptop.model
                            WHERE laptop.speed >= %s AND laptop.ram >= %s AND laptop.hd >= %s;''', (vel,ram,disco))
                result = cursor.fetchall()
                print(" Fabricante,  Modelo,  Velocidad,    RAM,   Disco,    Pantalla,  Costo ")
                for i in result:
                    print (i)
                print("")

                conexion.commit()
                print("Completado")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error")
        
            finally:
                cursor.close()
                conexion.close()
                print("Fin")
                print("")
                pass
            pass
        except ValueError:
            print("Ingrese numeros")
    else:
        print("Ingrese numero mayor a 0")

#################
#Ejercicio 3
#################
def ejercicioC(presupuesto, vel, color):
    color = color.lower()
    if color == "s":
        color = True
    else:
        color = False
        
    if presupuesto > 0 and vel > 0 and color == True:
        try:
            presupuesto = int(presupuesto)
            vel = int(vel)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=macario1270")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT pc.model AS ModeloPC, printer.model AS ModeloPrinter, (pc.price + printer.price) AS precio_Total, pc.speed AS PCVelocidad, pc.ram AS PCRAM, pc.hd AS PCDisco, printer.color AS PrintColor, printer.tipo AS PrintType
                            FROM pc, printer
                            WHERE pc.speed >= %s AND (pc.price + printer.price) <= %s AND printer.color = true;''', (vel,presupuesto))
                result = cursor.fetchall()
                print(" Modelo pc, Modelo pri,  Total,  Velocidad,   RAM,    Disco,    Color,  Tipo ")
                for i in result:
                    print (i)
                print("")

                conexion.commit()
                print("Completado")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error")
        
            finally:
                cursor.close()
                conexion.close()
                print("FIN")
                print("")
                pass
            pass
        except ValueError:
            print("Ingrese numeros")
    elif presupuesto > 0 and vel > 0 and color == False:
        try:
            presupuesto = int(presupuesto)
            vel = int(vel)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=macario1270")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT pc.model AS ModeloPC, printer.model AS ModeloPrinter, (pc.price + printer.price) AS precio_Total, pc.vel AS PCVelocidad, pc.ram AS PCRAM, pc.hd AS PCDisco, printer.color AS PrintColor, printer.tipo AS PrintType
                            FROM pc, printer
                            WHERE pc.vel >= %s AND (pc.price + printer.price) <= %s;''', (vel,presupuesto))
                result = cursor.fetchall()
                print(" Modelo pc,   Modelo pri,  Total,  Velocidad,   RAM,    Disco,    Color,  Tipo ")
                for i in result:
                    print (i)
                print("")

                conexion.commit()
                print("Completado")
        
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error")
        
            finally:
                cursor.close()
                conexion.close()
                print("Fin")
                print("")
                pass
            pass
        except ValueError:
            print("Ingresar numeros")        
    else:
        print("Numero invalido")

#################
#Ejercicio 4
#################
def ejercicioD(modelo, vel, ram, disco, costo):
    if modelo > 0 and vel > 0 and ram > 0 and disco > 0 and costo > 0:
        try:
            vel = int(vel)
            ram = int(ram)
            disco = int(disco)
            costo = int(costo)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=macario1270")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ WRITE ISOLATION LEVEL READ COMMITTED;")
                cursor.execute("SELECT * FROM insercion(%s, %s, %s, %s, %s, %s);", (fabricante, modelo, vel, ram, disco, costo))
                result = cursor.fetchall()
                print("PC ingresada con exito")
                print(" Fabricante, Modelo,  Velocidad,  RAM, Disco,  Costo ")
                for i in result:
                    print (i)
                print("")
                conexion.commit()
                print("Completado")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error")
            finally:
                cursor.close()
                conexion.close()
                print("FIN")
                print("")
                pass
            pass
        except ValueError:
            print("Ingresar numero")
    else:
        print("Numero invalida")

#################
#Ejercicio 5
#################
def ejercicioE(costo):
    if costo >= 0:
        try:
            costo = int(costo)
            try:
                conexion = psycopg2.connect("dbname=laboratorio12 user=postgres password=macario1270")
                cursor = conexion.cursor()
                cursor.execute("BEGIN TRANSACTION READ ONLY ISOLATION LEVEL READ COMMITTED;")
                cursor.execute('''
                            SELECT COUNT(DISTINCT pc.model) AS Numero_PC, (SELECT COUNT(*) 
									    FROM laptop
									    WHERE laptop.price > %s) AS Numero_Laptop, (SELECT COUNT(*) 
															   FROM printer
											     				   WHERE printer.price > %s) AS Numero_Printer
                            FROM pc
                            WHERE pc.price > %s;''', (costo,costo,costo))
                count2 = cursor.fetchone()
                result = "      "+str(count2[0])+"                   "+str(count2[1])+"                  "+str(count2[2])
                print("Cantidad PC,  Cantidad Laptop,  Cantidad Printer ")
                print(result)
                print("")
                conexion.commit()
                print("Completado")
            except (Exception, psycopg2.DatabaseError) as error:
                print("Error")
            finally:
                cursor.close()
                conexion.close()
                print("FIN")
                print("")
                pass
            pass
        except ValueError:
            print("Ingresar numero")
    else:
        print("Numero invalido")
