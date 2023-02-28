# dependencies
from threading import Thread, current_thread
# modules
from modules.connection import getLinks, add_new_link
from modules.analyzerLinks import analyzer

try:
    links_iniciales = ["https://expansion.mx/", "https://www.unotv.com/",
                       "https://www.weather.com/wx/today/", "https://www.ibm.com/", "https://es.wikipedia.org/wiki/Ajedrez",
                       "https://news.google.com/", "https://www.bbc.com/mundo", "https://www.lavozdemichoacan.com.mx/", "https://www.elsoldemorelia.com.mx/"]
    add_new_link(links_iniciales)
except Exception as e:
    pass

listaLinks = getLinks()


def fun_hilo():
    global listaLinks
    hilo = current_thread().getName()
    while True:
        try:
            if len(listaLinks) > 0:
                analyzer(listaLinks.pop())
                #  print(f"{hilo}") # aqui vemos que hilo esta trabajando
            else:
                listaLinks = getLinks()
                print(f"{hilo} refil")
                if len(listaLinks) < 1:
                    print(f"{hilo} esperando")
        except Exception as e:
            print(f"Error en {hilo}: ", e)


if __name__ == "__main__":
    hilo_uno = Thread(target=fun_hilo, name="hilo1")
    hilo_dos = Thread(target=fun_hilo, name="hilo2")
    hilo_tres = Thread(target=fun_hilo, name="hilo3")
    hilo_cuatro = Thread(target=fun_hilo, name="hilo4")
    hilo_cinco = Thread(target=fun_hilo, name="hilo5")
    hilo_seis = Thread(target=fun_hilo, name="hilo6")

    hilo_uno.start()
    hilo_dos.start()
    hilo_tres.start()
    hilo_cuatro.start()
    hilo_cinco.start()
    hilo_seis.start()

    print("Hilos inicializados")
