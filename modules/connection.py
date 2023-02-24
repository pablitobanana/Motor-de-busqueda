import pymongo
from pymongo import MongoClient


def connection_mongo():
    try:
        client = MongoClient('localhost', 27017)
        db = client['motor']
        collection = db['urls']
        return collection
    except Exception as ex:
        print("No se pudo conectar en la base de datos: ",ex)


def getLinks():
    listaLinks = []
    connection = connection_mongo()
    try:
        for elements in connection.find({"checked": False}):
            listaLinks.append(elements)
    except Exception as ex:
        print( "no se pudieron extraer los links: ",ex )
    return listaLinks


def is_checked(url):
    try:
        connection = connection_mongo()
        my_query = {"_id": url['_id']}
        newvalues = {"$set": {"checked": True}}
        connection.update_one(my_query, newvalues)
    except Exception as e:
        print("no se pudo marcar como checked: ",e)


def add_new_link(url_list):
    for url in url_list:
        document_structure = {"_id": url, "checked": False}
        try:
            connection = connection_mongo()
            connection.insert_one(document_structure)
            print("Agregado exitosamente")
        except Exception as e:
            print("no se pudieron agregar: ",url,"\n",e)

