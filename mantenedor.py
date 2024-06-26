from os import system
from menus import *
import json

def generarArchivoReporte(biblioteca):
    with open("Reportes_biblioteca_mundo_libro.json", "w") as archivo:
        json.dump(biblioteca, archivo, indent=1)


def abrirArchivo():
    with open("biblioteca.json" , "r") as archivo:
        biblioteca = json.load(archivo)
        return biblioteca

def limpiarPantalla():
    system("cls")

def validarId():
    while True:
        try:
            id = int(input("Ingresa el ID : "))
            return id
        except:
            print("El id debe ser un numero.")

def idAutomatico(biblioteca):
    id = len(biblioteca["Autor"])+1
    return id
    
def mostrarAutores(biblioteca):
    limpiarPantalla()
    print("MOSTRAR AUTORES")
    for i in biblioteca["Autor"]:
        print(i)

####
def agregarAutores(biblioteca):
    limpiarPantalla()
    print("AGREGAR AUTOR")
    autorID = idAutomatico(biblioteca)
    nombre = input("Nombre : ")
    nacionalidad = input("Nacionalidad : ")

    autor = {
        "AutorID": autorID,
        "Nombre": nombre,
        "Nacionalidad": nacionalidad
    }

    biblioteca["Autor"].append(autor)
    return biblioteca
        
def editarAutores(biblioteca):
    limpiarPantalla()
    print("EDITAR AUTOR")
    id = validarId()
    for i in biblioteca["Autor"]:
        if id == i["AutorID"]:
            print(f"Modificaras: {i}")
            nombre = input("Cambiar nombre : ")
            nacionalidad = input("Cambiar nacionalidad : ")

            i["Nombre"] = nombre
            i["Nacionalidad"] = nacionalidad

    return biblioteca

def eliminarAutores(biblioteca):
    limpiarPantalla()
    print("ELIMINAR AUTOR")
    id = validarId()
    for i in biblioteca["Autor"]:
        if i["AutorID"] == id:
            biblioteca["Autor"].remove(i)
            print("Autor eliminado")
        else:
            print("El ID no existe")
    return biblioteca

def decisionPrincipal():
    while True:
        opcion = input("Donde quieres ir : ")
        if opcion == "1":
            menuMantenedores()
            decisionMantenedores(biblioteca)
            break
            
        if opcion == "2":
            generarReporte(biblioteca)
            break

def decisionMantenedores(biblioteca):
    while True:
        print("")
        opcion = input("Tu opcion : ")
        if opcion == "1":
            biblioteca = agregarAutores(biblioteca)

        if opcion == "2":
            biblioteca = editarAutores(biblioteca)

        if opcion == "3":
            biblioteca = eliminarAutores(biblioteca)

        if opcion == "4":
            mostrarAutores(biblioteca)

        if opcion == "5":
            menuPrincipal()
            decisionPrincipal()
            limpiarPantalla()
            break

def generarReporte(biblioteca):

    cantidadLibros = 0

    #CANTIDAD DE CADA LIBRO
    for i in biblioteca["Prestamo"]:
        for j in biblioteca["Prestamo"]:
            if j["LibroID"] == i["LibroID"]:
                cantidadLibros += 1
        print(cantidadLibros)
        cantidadLibros = 0


        #libroBuscado = i["LibroID"]
        #print(f"{i}")


    
    """#Libro
    for i in biblioteca["Libro"]:
        if libroBuscado == i["LibroID"]:
            autorBuscado = i["AutorID"]
            break

    #Autor
    for i in biblioteca["Autor"]:
        if autorBuscado == i["AutorID"]:
            autorBuscado = i["Nombre"]
            print(f"El autor es {autorBuscado}")
            break"""
    

biblioteca = abrirArchivo()
menuPrincipal()
decisionPrincipal()
