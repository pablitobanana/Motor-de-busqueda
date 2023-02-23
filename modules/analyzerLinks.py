from modules.connection import connection_mongo


def analyzer(url):
    print(url['_id'])
    connection = connection_mongo()
    my_query = {"_id":url['_id']}
    newvalues = { "$set": { "checked": True} }
    connection.update_one(my_query, newvalues)
