# dependencies
from threading import Thread, current_thread
# modules
from modules.connection import getLinks, add_new_link
from modules.analyzerLinks import analyzer

try:
    links = ["https://expansion.mx/","https://www.unotv.com/","https://www.weather.com/wx/today/"]
    add_new_link(links)
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
            else:
                listaLinks = getLinks()
                print(f"{hilo} refil")
                if len( listaLinks ) < 1:
                    print(f"fin {hilo}")
                    break
        except Exception as e:
            print(f"Error en {hilo}: ", e)


if __name__ == "__main__":
    hilo_uno = Thread(target=fun_hilo, name="hilo1")
    hilo_dos = Thread(target=fun_hilo, name="hilo2")
    hilo_tres = Thread(target=fun_hilo, name="hilo3")

    hilo_uno.start()
    hilo_dos.start()
    hilo_tres.start()

    print("Hilos inicializados")
