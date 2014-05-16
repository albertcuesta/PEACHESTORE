__author__ = 'albert cuesta'

import os.path
class database:

    def listaraplicaiones(self):
       result = []
       with open("database/data/aplicaciones.txt", mode='r+', encoding='utf-8') as file:
           resultado = file.read()
       texto = resultado.split("\n")
       for linea in texto:
           result.append(linea.split(","))
           return result

    def listaraplicacionespago(self):
        aplicaciones=[]
        fo = open("database/data/aplicacionesPago.txt", mode='r', encoding='utf-8')
        for line in fo:
            return line
        fo.close()


    def añadiraplicacionpago(self, nombre, proveedor, fecha, precio, descargas,puntuacion,comentarios):
        aplicacion = []
        with open("database/data/aplicacionesPago.txt", mode='a',encoding='utf-8')as archivo1:
            archivo1.write(nombre+","+proveedor+","+fecha+","+precio+","+descargas+","+puntuacion+","+comentarios+"\n")
            print ("app insertada")

    def añadiraplicacionfree(self, nombre, proveedor, fecha, precio, descargas,puntuacion,comentarios):
        aplicacion = []
        with open("database/data/aplicaciones.txt", mode='a',encoding='utf-8')as archivo:
            archivo.write(nombre+","+proveedor+","+fecha+","+precio+","+descargas+","+puntuacion+","+comentarios+"\n")
            print ("app insertada")

    def sumarDescarga(self, nombre, pathToDb="database/data/aplicaciones.txt"):
        if os.path.isfile('database/data/aplicaciones.txt'):
            file = open(pathToDb, 'r')
            llista = file.readlines()
            file.close()
            trobat = False
            with open(pathToDb, 'w') as file:
                for linia in llista:
                    if linia.split(";")[0] != nombre:
                        file.write(linia)
                    else:
                        linia1 = linia.split(";")
                        descargues = int(linia.split(";")[4])
                        resultat = linia1[0]+";"+linia1[1]+";"+linia1[2]+";"+linia1[3]+";"+str(descargues+1)+";"+linia1[5]+";"+linia1[6]+";"+linia1[7]
                        file.write(resultat)
                        trobat = True
        else:
            print("Error! No se ha podido encontrar el fichero de aplicaciones!")
        return trobat
