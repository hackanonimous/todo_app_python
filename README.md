# Proyecto ToDo APP en python
 #### Proyecto todo app, haciendo uso de la libreria para interfacez graficas en python `flet`.

 ## Instalación
 #### Pasos para correr el proyecto de manera local
 > [!TIP]
 > Todos comandos descritos en la guia seran ejecutados en **GitBash**
 ### 1. Clonar el repositorio
 ```bash
 git clone https://github.com/hackanonimous/todo_app_python.git
 ```
 este comando creara la carpeta `todo_app_python`
 ### 2. Acceder a la carpeta del repositorio
 ```bash
 cd todo_app_python
 ```
 ### 3. Eliminamos la carpeta `.git`
 ```python
 rm -rf .git
 ```
 ### 4. Crear un entorno virtual
 ```bash
 python -m venv .todo_venv
 ```
 ### 5. Activamos entorno virtual
 #### Windows:
 ```bash
source /.todo_venv/Script/activate
 ```
 #### Linux:
 ```bash
 source /.todo_venv/bin/activate
 ```
 ### 5. Instalar dependencias
 ```bash
 pip install -r requirements.txt
 ```
 ### 6. Ejecutar el programa
 ```bash
 flet run main.py
 ```