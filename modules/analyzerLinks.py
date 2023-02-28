# dependencies
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from collections import Counter
import re
import nltk
import ssl
nltk.download('stopwords')
ssl._create_default_https_context = ssl._create_unverified_context

# modules

from modules.connection import is_checked, add_new_link, add_words_and_titles, ranking

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def get_new_links(bs, url_element):
    try:
        listaURLS = []
# encontramos todas las etiquetas a para obtener los links
        for enlaces in bs.find_all("a"):
            # validamos que sea un link o url
            if is_valid_url(enlaces.get("href")):
                resultado = urlparse(enlaces.get("href"))
# lo comvertimos en un link sin parametros y lo retornamos como un conjunto (set) para que quite los elementos repetidos
                url_sin_params = f"{resultado.scheme}://{resultado.netloc}{resultado.path}"
                listaURLS.append(url_sin_params)
        return set(listaURLS)
    except Exception as e:
        print("No se pudo optener los link: ", url_element['_id'], "\n", e)


def analyzing_text_page(bs):
    words_and_titles = {}
    try:
        words_and_titles["title"] = bs.title.string
    except Exception:
        words_and_titles["title"] = None
        #  print("no se pudo extraer el title o no cuenta con uno")
    try:
        words_and_titles["h1"] = bs.h1.string
    except Exception:
        words_and_titles["h1"] = None
        #  print("no se pudo extraer el h1 o no cuenta con uno")
    try:
        for parrafos in bs.find_all("p"):
            if len(parrafos.string) > 30:
                words_and_titles["p"] = parrafos.string
                break
            else:
                words_and_titles["p"] = None
    except Exception:
        words_and_titles["p"] = None
        #  print("no se pudo extraer el h1 o no cuenta con uno")
    try:
        text = bs.get_text()

# Limpiar el texto eliminando caracteres no alfabéticos y stopwords
        stop_words_en = set(stopwords.words('english'))
        stop_words_es = set(stopwords.words('spanish'))
        clean_text = [word.lower() for word in re.findall(r'\b\w+\b', text) if word.lower()
                      not in stop_words_en and word.lower() not in stop_words_es]

# Contar la frecuencia de cada palabra
        word_counts = Counter(clean_text)

# obtener las 10 palabras más repetidas
        num = 0
        words_and_titles["palabras"] = []
        for word, count in word_counts.most_common(10):
            num += 1
            words_and_titles["palabras"].append(word)
    except Exception:
        print("no se pudo extraer las palabras de la pagina")

    return words_and_titles


def analyzer(url):
    is_checked(url)
    try:
        html = urlopen(url['_id'])
        bs = BeautifulSoup(html, 'html.parser')
        new_links = get_new_links(bs, url)
        not_added = ranking(new_links)
        add_new_link(not_added)
        words_to_add = analyzing_text_page(bs)
        add_words_and_titles(url, words_to_add)
    except Exception as ex:
        print("no se pudo analizar la pagina: ", url['_id'])
