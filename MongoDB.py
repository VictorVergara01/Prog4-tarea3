from this import d
import pymongo
myclient= pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb= myclient["Diccionario"]
mycol= mydb['diccionario']

def principal():
    menu="""
a) Agregar nueva palabra
b) Editar palabra existente
c) Eliminar palabra existente
d) Ver listado de palabras
e) Buscar significado de palabra
f) Salir
Elige: """
    eleccion = ""
    while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            palabra = input("Ingresa la palabra: ")
            # Comprobar si no existe
            posible_significado = mycol.find_one({"Palabra": {'$eq': palabra}})
            if posible_significado:
                print(f"La palabra '{palabra}' ya existe")
            else:
                significado = input("Ingresa el significado: ")
                agregar_palabra(palabra, significado)
                print("Palabra agregada")
        if eleccion == "b":
            palabra = input("Ingresa la palabra que quieres editar: ")
            nuevo_significado = input("Ingresa el nuevo significado: ")
            editar_palabra(palabra, nuevo_significado)
            print("Palabra actualizada")
        if eleccion == "c":
            palabra = input("Ingresa la palabra a eliminar: ")
            eliminar_palabra(palabra)
            print("Palabra eliminada")
        if eleccion == "d":
            print("=== Lista de palabras ===")
            for x in mycol.find({},{ "_id": 0, "significado": 0}):
                print(x)
        if eleccion == "e":
            palabra = input(
                "Ingresa la palabra de la cual quieres saber el significado: ") 
            significado = mycol.find_one({"Palabra": {'$eq': palabra}})
            if significado:
                    print(significado)
            else:
                print("Palabra no encontrada")

def agregar_palabra(palabra, significado):
    sentencia = {"Palabra": palabra, "significado": significado}
    mycol.insert_one(sentencia)


def editar_palabra(palabra, significado):
    consulta={"Palabra": palabra}
    nuevo_valor = {"$set":{"Palabra": palabra, "Significado": significado}}
    mycol.update_one(consulta,nuevo_valor)

def eliminar_palabra(palabra):
    consulta = {"Palabra": palabra}
    mycol.delete_one(consulta)
    

if __name__ == '__main__':
  principal()