from modules.connection import connection_mongo

def getLinks():
    listaLinks = []
    connection = connection_mongo()
    try:
        for elements in connection.find({"checked":False}):
            listaLinks.append(elements)
    except Exception as ex:
        raise ex

    return listaLinks
