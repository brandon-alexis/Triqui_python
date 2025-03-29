# Triqui 

Desarrollo de un juego clasico de Triqui 

## Requisitos
- Python >= 3
- pip 
- pygame

## Instalacion de dependencias

### Instalacion de python
Si no tienes python instalado, hazlo desde la pagina oficial de python por [aqui](https://www.python.org/downloads/)

Para probar el proyecto verifica que tienes python instalado desde la consola de tu sistema operativo

### Verificacion de instalacion de python
```shell
python --version
```

### Instalacion de pip
Despues de verifivar que tiene python instalado, necesitamos instalar el gestor de paquetes de python llamado pip

```shell
python -m pip install --upgrade pip
```

Si no te funciona este metodo, intenta instalarlo de la siguiente manera

Descarga el instalador de pip [get-pip.py](https://bootstrap.pypa.io/get-pip.py), despues que lo hayas descargado ve a la **terminal de tu sistema** y ve a la ruta donde guardaste el archivo **get-pip.py** copiando primero el texto de la ruta donde esta, por ejemplo

Supongamos que lo guardamos en *C:\Users\TuUsuario\Downloads*

teniendo en cuenta esto en el **cmd** escribe 

```shell
cd C:\Users\TuUsuario\Downloads\
```

> **Recuerda esta ruta solo es de ejemplo**

ahora si escribe el siguiente comando

```shell
python get-pip.pip
```

Ahora deberia empezar a instalarse en tu sistema sin problema


### Verificacion de instalacion de pip
Verifica si tienes pip instalado desde la console de tu sistema operativo

```shell
pip --version
```

Ahora instala la libreria de pygame de la siguiente manete
```shell
pip install pygame-ce
```

## Ejecutar

Despues de tener todas las dependencias necesarias para ejecutar el proyecto sigue los siguiente pasos:

> Si tienes **git** instalador ejecuta lo siguiente

```shell
git clone https://github.com/brandon-alexis/Triqui_python.git
```

> en caso que no lo tengas instalado

Dale al boton **Code**, luego **Download ZIP** para obtener el archivo comprimido con la carpeta del juego

Entra a la carpeta **Triqui_python** y ejecuta el siguiente comando 

```shell
python src/main.py
```

o tambien

```shell
make run
```


Tambien puedes ejecutarlo abriendo el proyecto y ejecutandolo desde el boton de ejecutar que te proporciona tu editor de codigo.

Listo deberia de aparecerte la pantalla del juego






