# dependencies
from threading import Thread, current_thread
# modules
from modules.getLinks import getLinks
from modules.analyzerLinks import analyzer

listaLinks = getLinks()


def fun_hilo():
    global listaLinks
    hilo = current_thread().getName()
    while True:
        try:
            if len(listaLinks) < 1:
                listaLinks = getLinks()
                print(f"{hilo} refil")
                if len( listaLinks ) < 1:
                    print(f"fin {hilo}")
                    break
            else:
                analyzer(listaLinks.pop())
        except Exception as e:
            print(f"Error en {hilo}: ", e)


if __name__ == "__main__":
    hilo_dos = Thread(target=fun_hilo, name="hilo2")
    hilo_tres = Thread(target=fun_hilo, name="hilo3")
    hilo_uno = Thread(target=fun_hilo, name="hilo1")

    hilo_dos.start()
    hilo_tres.start()
    hilo_uno.start()

    print("Hilos inicializados")
