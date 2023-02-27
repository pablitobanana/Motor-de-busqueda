# Requerimientos
Estando dentro del proyecto ejecutaremos los siguientes comandos
## Python

### Paso1 :
```sh
$ pip install -r requeriments.txt
```
## Vue
### Paso 2:
```sh
$ cd buscador
$ npm install
```
# Ejecución de motor de busqueda
(esto no incluye la pagina web)
## Levantar servicio mongo
ejecutaremos el siguiente omando para levantar el servicio de mongo
```sh
$ mongod
```
Para empezar la ejecucion del motor de busqueda, dentro del proyecto ejecutaremos el programa `main.py`
```sh
$ python3 main.py
```
Esto ara que el motor de busqueda comience a ejecutarce.
> NOTA: este programa contiene un ciclo infinito, este listo para matar el servicio.

## Como matar el servicio
### windows:
Ejecute los siquientes comandos para terminar el proceso
```sh
> tasklist
```
Aparecera una lista de los servicios, identifique el que se llama py.exe y su PID.
Una vez hecho, ejecute el siguiente comando.
```sh
> taskkill /f /PID [PID del servicio]
```
Si no se detiene, apaque la computadora :3 .

## Inicializar la API
Para consumir los datos utilizamos una api en Flask, sigua los siguientes pasos para iniciarla.

### Paso 1:
Agregar la variable de entorno.
Para el caso de una computadora mac se escribe `export`, para el caso de windows es `set`, pero el valor es el mismo.
```sh
$ export FLASK_APP=api.py
```
### Paso 2: 
Inicializar el servidor.
```sh
$ flask run
```
## Visualizar la pagina y resultados
Para inicializar la pagina web entraremos a la carpeta `buscador` y ejecutaremos `npm run dev`.
```sh
$ cd buscador
$ npm run dev
```
Vaya a la direccion asignada y seria todo.
