import pymongo
from pymongo import MongoClient


def connection_mongo():
    try:
        client = MongoClient('localhost', 27017)
        db = client['motor']
        collection = db['urls']
        return collection
    except Exception as ex:
        print("No se pudo conectar en la base de datos: ", ex)


def getLinks():
    listaLinks = []
    connection = connection_mongo()
    try:
        for elements in connection.find({"checked": False}):
            listaLinks.append(elements)
    except Exception as ex:
        print("no se pudieron extraer los links: ", ex)
    return listaLinks


def is_checked(url):
    try:
        connection = connection_mongo()
        my_query = {"_id": url['_id']}
        newvalues = {"$set": {"checked": True}}
        connection.update_one(my_query, newvalues)
    except Exception as e:
        print("no se pudo marcar como checked: ", e)


def add_new_link(url_list):
    listaURLS = []
    for url in url_list:
        document_structure = {"_id": url, "checked": False, "ranking":0}
        listaURLS.append(document_structure)
    try:
        connection = connection_mongo()
        connection.insert_many(listaURLS)
    except Exception as e:
        pass
            #  print("no se pudieron agregar: ", len(listaURLS))

def ranking(urls_unchecked):
    connection = connection_mongo()
    unadded = []
    for urls in urls_unchecked:
        my_query = {"_id": urls}
        link = connection.find_one(my_query)
        if link != None:
            try:
                rank = link["ranking"] + 1
                newvalues = {"$set": {"ranking": rank }}
                connection.update_one(my_query, newvalues)
            except Exception as e:
                print("no se pudo agregar al ranking")
        else:
            unadded.append(urls)
    return unadded


def add_words_and_titles(url,words_and_titles):
    try:
        connection = connection_mongo()
        my_query = {"_id": url['_id']}
        newvalues = {"$set": words_and_titles}
        connection.update_one(my_query, newvalues)
    except Exception:
        print("no se pudo agrear las palabras claves de: ",url['_id'] )

def serching(request):
    palabras = request.split()
    try:
        connection = connection_mongo()
    except Exception:
        pass
    lista_links_encontrados = []
    for word in palabras:
        try:
            links = connection.find({"palabras": word})
            if links != None:
                for link in links:
                    lista_links_encontrados.append(link)
        except Exception:
            pass
    lista_acomodada = sorted(lista_links_encontrados, key=lambda links : links['ranking'], reverse=True)
    return lista_acomodada
