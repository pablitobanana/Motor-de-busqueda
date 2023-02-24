from modules.connection import is_checked, add_new_link
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def get_and_save_links(url_element):
    try:
        html = urlopen(url_element['_id'])
        bs = BeautifulSoup(html.read(), 'html.parser')
        listaURLS = []
        for enlaces in bs.find_all("a"):
            if is_valid_url(enlaces.get("href")):
                resultado = urlparse(enlaces.get("href"))
                url_sin_params= f"{resultado.scheme}://{resultado.netloc}{resultado.path}"
                #  print(url_sin_params)
                listaURLS.append(url_sin_params)
        add_new_link(set( listaURLS ))
    except Exception as e:
        print("No se pudo acceder al link: ",url_element['_id'],"\n",e)

def analyzer(url):
    is_checked(url)
    get_and_save_links(url)


