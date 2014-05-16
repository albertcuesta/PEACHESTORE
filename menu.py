__author__ = 'Albert cuesta'

import PEACHESTORE.database.Database as database


def menu(self=None):
        print('\t BENVINGUTS A PEACHESTORE')
        print('\t [1]: Mostrar aplicacions')
        print('\t [2]: Registrar aplicacions')
        print('\t [3]: Modificar aplicacions')
        print('\t [4]: sumar descarga')
        opcio = int(input('opcion?'))
        if opcio == 1:
            print("=== aplicacions ===")
            print('\t [1]: Mostrar aplicaciones gratis')
            print('\t [2]: Mostrar aplicaciones pago')
            opcio1 = int(input('opcion1?'))
            if opcio == 1:
                result = database.database.listaraplicaiones(self)
                print(result)
            if opcio == 2:
                result2 = database.database.listaraplicacionespago(self)
                print(result2)
        if opcio == 2:
            print("=== aplicacions ===")
            print('\t [1]: registrar aplicaciones gratis')
            print('\t [2]: registrar aplicaciones pago')
            opcio2 = int(input('opcion2?'))
            if opcio2 == 1:
                print("=== aplicacions free===")
                nombre = input('\tIntroduzca nombre app: ')
                proveedor = input('\tIntroduzca proveedor: ')
                fecha = input('\tIntroduzca fecha: ')
                precio = input('\tIntroduzca su precio: ')
                descargas = input('\tIntroduzca su descargas: ')
                puntuacion = input('\tIntroduzca su puntuacion: ')
                comentarios = input('\tIntroduzca su comentarios: ')
                database.database.añadiraplicacionpago(self,nombre,proveedor,fecha, precio, descargas,puntuacion,comentarios)
            if opcio2== 2:
                print("=== aplicacions pago ===")
                nombre = input('\tIntroduzca nombre app: ')
                proveedor = input('\tIntroduzca proveedor: ')
                fecha = input('\tIntroduzca fecha: ')
                precio = input('\tIntroduzca su precio: ')
                descargas = input('\tIntroduzca su descargas: ')
                puntuacion = input('\tIntroduzca su puntuacion: ')
                comentarios = input('\tIntroduzca su comentarios: ')
                database.database.añadiraplicacionfree(self,nombre,proveedor,fecha, precio, descargas,puntuacion,comentarios)
        if opcio== 3:
            print("=== Modificar aplicacions ===")
            print('\t [1]: modificar aplicaciones gratis')
            print('\t [2]: modificar aplicaciones pago')
            opcio2 = int(input('opcion2?'))
            if opcio2 == 1:
                print("=== aplicacions free===")
                nombre = input('\tIntroduzca nombre app: ')
                proveedor = input('\tIntroduzca proveedor: ')
                fecha = input('\tIntroduzca fecha: ')
                precio = input('\tIntroduzca su precio: ')
                descargas = input('\tIntroduzca su descargas: ')
                puntuacion = input('\tIntroduzca su puntuacion: ')
                comentarios = input('\tIntroduzca su comentarios: ')
                database.database.añadiraplicacionpago(self,nombre,proveedor,fecha, precio, descargas,puntuacion,comentarios)
            if opcio2== 2:
                print("=== modificar aplicacions pago ===")
                nombre = input('\tIntroduzca nombre app: ')
                proveedor = input('\tIntroduzca proveedor: ')
                fecha = input('\tIntroduzca fecha: ')
                precio = input('\tIntroduzca su precio: ')
                descargas = input('\tIntroduzca su descargas: ')
                puntuacion = input('\tIntroduzca su puntuacion: ')
                comentarios = input('\tIntroduzca su comentarios: ')
                database.database.añadiraplicacionfree(self,nombre,proveedor,fecha, precio, descargas,puntuacion,comentarios)
        if opcio== 4:
            print("=== sumar descarga ===")
            database.database.sumarDescarga(self,'facebook',"database/data/aplicaciones.txt")
            print




menu()


