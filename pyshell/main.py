import sys
import os
import re
import shutil
import subprocess
import ctypes
from rich import print
from rich.progress import Progress
from time import sleep

def inicialisador():
    global directory
    directory = os.getcwd()
    banner()
    main()

####################################################
# Banner
####################################################
def banner():
    banner = """
    [bold yellow]python[/bold yellow] [bold]main.py[/bold]
    \n
    [bold blue]██████╗ ██╗   ██╗[/bold blue][bold #FFFF00]███████╗██╗  ██╗███████╗██╗     ██╗[/bold #FFFF00]    
    [bold blue]██╔══██╗╚██╗ ██╔╝[/bold blue][bold #FFFF00]██╔════╝██║  ██║██╔════╝██║     ██║[/bold #FFFF00]
    [bold blue]██████╔╝ ╚████╔╝ [/bold blue][bold #FFFF00]███████╗███████║█████╗  ██║     ██║[/bold #FFFF00]
    [bold blue]██╔═══╝   ╚██╔╝  [/bold blue][bold #FFFF00]╚════██║██╔══██║██╔══╝  ██║     ██║[/bold #FFFF00]
    [bold blue]██║        ██║   [/bold blue][bold #FFFF00]███████║██║  ██║███████╗███████╗███████╗[/bold #FFFF00]
    [bold blue]╚═╝        ╚═╝   [/bold blue][bold #FFFF00]╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝[/bold #FFFF00]
    \n 
    [bold #f03ced]Terminal hecha especificamente para [bold blue]py[/bold blue][bold #FFFF00]thon[/bold #FFFF00] \n 
    vercion de la terminal [bold #13c8dc]1.5[/bold #13c8dc][/bold #f03ced]
    """
    print(banner)

####################################################
# Comandos
####################################################
def list_command():
    list = """
    [bold #1E90FF]# comandos del programa[/bold #1E90FF]
    - [bold #32CD32]pysh -h, -h, help(), help[/bold #32CD32]: muestra la lista de comandos
    - [bold #32CD32]pysh -clr, clr, clear, cls[/bold #32CD32]: limpia la consola
    - [bold #32CD32]pysh -exit, exit(), exit[/bold #32CD32]: cierra el programa
    - [bold #32CD32]pysh --version[/bold #32CD32]: para ver la verción de la terminal 
    - [bold #32CD32]pysh --view, dir, ls [/bold #32CD32]: para ver los archivos y carpetas de la carpeta actual
    - [bold #32CD32]pysh --del-arch (nombre de tu archivo/ubicación de tu archivo)[/bold #32CD32]: para eliminar los archivos de tu directorio 
    - [bold #32CD32]pysh --del-carp (nombre de tu carpeta/ubicación de tu carpeta)[/bold #32CD32]: para eliminar las carpetas de tu directorio
    - [bold #32CD32]pysh --crt-arch (nombre de tu archivo y su extencion)[/bold #32CD32]: para crear un archivo 
    - [bold #32CD32]pysh --crt-carp (nombre de tu carpeta)[/bold #32CD32]: para crear una carpeta
    - [bold #32CD32]pp-pysh --push-admin[/bold #32CD32]: para entrar en modo administrador
    - [bold #32CD32]cd (nombre de la ruta a la que quieras ir)[/bold #32CD32]: para cambiar de directorio
    \n
    [bold red]# comandos de python [/bold red]
    - [bold #e68aa9]print()[/bold #e68aa9]: muestra un mensaje en la consola
    - [bold #e68aa9]input()[/bold #e68aa9]: pide un mensaje en la consola
    - [bold #e68aa9]len()[/bold #e68aa9]: devuelve la longitud de un objeto
    \n
    [bold #FFFF00]# Instalar extenciones[/bold #FFFF00]
    - [bold #8000FF]Install python[/bold #8000FF] : para instalar python
    - [bold #8000FF]Install pip[/bold #8000FF] : para instalar pip
    - [bold #8000FF]pip install (nombre de la extencion)[/bold #8000FF] : para instalar una extencion
    - [bold #8000FF]pip uninstall (nombre de la extencion)[/bold #8000FF] : para desinstalar una extencion
    \n
    [bold #09b843]# Comandos para administrar python[/bold #09b843]
    - [bold #b76f0a]pysh-v-pp [/bold #b76f0a]: ver la verción de python
    - [bold #b76f0a]pysh-v-pip [/bold #b76f0a]: ver la verción de pip
    - [bold #b76f0a]pysh-update-pp [/bold #b76f0a]: actualizar python a su ultima verción
    - [bold #b76f0a]pysh-update-pip [/bold #b76f0a]: actualizar pip a su ultima verción
    \n
    [bold #62bfde]# Quieres usar tu editor de codigo?[/bold #62bfde] [bold red]Solo si lo tienes instalado[/bold red] 
    - [bold #1E90FF]vscode[/bold #1E90FF] : para abrir [#00CED1]Visual Studio Code[/#00CED1]
    - [bold #FFFF00]trae[/bold #FFFF00] : para abrir [#00CED1]Trae IA[/#00CED1]
    \n
    [bold red]# Abrir github[/bold red]
    - [bold #FFFF00]github[/bold #FFFF00] : para abrir [#00CED1]github[/#00CED1]
    """
    print(list)

####################################################
# Inicio del prograna
####################################################
def main():
    msg = "Para ver la lista de los comandos coloque [bold green]'pysh -h'[/bold green]"
    print(msg)
    validation_request()

####################################################
# Validación
####################################################
def validation_request():
    ####################################################
    # la ruta de directorio 
    ####################################################
    global directory 
    while True:
        request = input(f"pysh / {directory}>> ")
        system_validation(request)

def system_validation(request):
    ####################################################
    # la ruta de directorio 
    ####################################################
    global directory

    # Comandos
    if request == "pysh -h" or request == "-h" or request == "help()" or request == "help":
        list_command()
    # print
    elif request.startswith("print(") and request.endswith(")"):
        match = re.search(r'print\(["\'](.*)["\']\)', request)
        if match:
            print(f"[bold #FFFF00]{match.group(1)}[/bold #FFFF00]")
        else:
            print("[bold red]Error de sintaxis[/bold red]")
    # input
    elif request.startswith("input(") and request.endswith(")"):
        match = re.search(r'input\(["\']?(.*?)["\']?\)', request)
        if match is not None:
            prompt_text = match.group(1) if match.group(1) else ">> "
            msg = input(f"{prompt_text}")
            print(f"[bold #FFFF00]>> {msg}[/bold #FFFF00]")
        else:
            print("[bold red]Error de sintaxis en input()[/bold red]")
    # len
    elif request.startswith("len(") and request.endswith(")"):
        match = re.search(r'len\(["\'](.*)["\']\)', request)
        if match:
            print(f"[bold #FFFF00]{len(match.group(1))}[/bold #FFFF00]")
        else :
            print("[bold red]Error de sintaxis[/bold red]")
    # limpiar la consola
    elif request == "pysh -clr" or request == "clr" or request == "clear" or request == "cls":
        clearsh()
    # instalar python y pip
    # install python 
    elif request == "Install python":
        subprocess.run(["winget", "install", "--id", "Python.Python", "-e"], shell=True)
        progress_bar_download()
        vercion_pp = subprocess.run(["python", "--version"], capture_output=True, text=True)
        print(f"[bold #FFFF00]verción de python : {vercion_pp.stdout.strip()}[/bold #FFFF00]")
    # install pip
    elif request == "Install pip":
        subprocess.run(["python", "-m", "ensurepip"], shell=True)
        progress_bar_download()
        version_pip = subprocess.run(["pip", "--version"], capture_output=True, text=True)
        print(f"[bold #FFFF00]verción de pip : {version_pip.stdout.strip()}[/bold #FFFF00]")
    # instalar extenciones
    elif request.startswith("pip install") and request.endswith(""):
        ext = request.split("pip install ", 1)[1].strip()
        if ext:
            extencion = ext.group(1)
            subprocess.run(["pip", "install", extencion], shell=True)
            print(f"[bold #FFFF00]extencion [bold green]{extencion}[/bold green] instalada[/bold #FFFF00]")
    # desistalar extenciones
    elif request.startswith("pip uninstall") and request.endswith(""):
        match = re.search(r'pip uninstall (.*)', request)
        if match:
            extencion = match.group(1)
            subprocess.run(["pip", "uninstall", extencion], shell=True)
            print(f"[bold #FFFF00]extencion [bold green]{extencion}[/bold green] desinstalada[/bold #FFFF00]")
    # ver la vercion de python y de pip
    # python version
    elif request == "pysh-v-pp":
        vercion_pp = subprocess.run(["python", "--version"], capture_output=True, text=True)
        print(f"[bold #FFFF00]verción de python : {vercion_pp.stdout.strip()}[/bold #FFFF00]")
    # pip version
    elif request == "pysh-v-pip":
        version_pip = subprocess.run(["pip", "--version"], capture_output=True, text=True)
        print(f"[bold #FFFF00]verción de pip : {version_pip.stdout.strip()}[/bold #FFFF00]")
    # actualizar python
    elif request == "pysh-update-pp":
        print("actualizando [bold blue]py[/bold blue][bold #FFFF00]thon[/bold #FFFF00] a la ultima verción")
        subprocess.run(["winget", "upgrade", "Python.Python"], shell=True)
    # actualizar pip
    elif request == "pysh-update-pip":
        print("[bold red]actualizando pip a la ultima verción[/bold red]")
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "pip"], shell=True)
    # abrir vscode y trae
    # vscode
    elif request == "vscode":
        progress_bar_open_editor_code()
        os.system("code .")
    # trae
    elif request == "trae":
        progress_bar_open_editor_code()
        os.system("trae")
    # github
    elif request == "github":
        with Progress() as progress:
            open_github = progress.add_task("[cyan]Abriendo github...", total=100)
            while not progress.finished:
                progress.update(open_github, advance=25)
                sleep(0.3)
        os.system("start https://github.com/")
    # ver la version de la terminal
    elif request == "pysh --version":
        msg_version = "[bold #f000ff ]verción de [/bold #f000ff][bold blue]py[/bold blue][bold #FFFF00]shell[/bold #FFFF00] : [green]1.05[/green]"
        print(msg_version)
    # ver los archivos y carpetas de la carpeta actual
    elif request == "pysh --view" or request == "dir" or request == "ls":
        with Progress() as progress:
            upload_view = progress.add_task("[cyan]Cargando archivos y carpetas...", total=100)
            while not progress.finished:
                progress.update(upload_view, advance=25)
                sleep(0.3)
        print("[bold #FFFF00]\nArchivos y carpetas de la carpeta actual\n[/bold #FFFF00]")
        os.system("dir")
    # codigo para eliminar los archivos y carpetas de los directiorios
    # eliminar los archivos
    elif request.startswith("pysh --del-arch"):
        archivo = request.replace("pysh --del-arch ", "").strip()
        if not archivo:
            print("[bold red]Error: Debes especificar un archivo a eliminar[/bold red]")
        elif not os.path.exists(archivo):
            print(f"[bold red]Error: El archivo '{archivo}' no existe[/bold red]")
        else:
            try:
                os.remove(archivo)
                print(f"[bold #FFFF00]Archivo '{archivo}' eliminado exitosamente[/bold #FFFF00]")
            except PermissionError:
                print(f"[bold red]Error: No tienes permisos para eliminar '{archivo}'[/bold red]")
            except Exception as e:
                print(f"[bold red]Error al eliminar '{archivo}': {e}[/bold red]")
    # eliminar las carpetas
    elif request.startswith("pysh --del-carp"):
        carpeta = request.replace("pysh --del-carp", "").strip()
        if not carpeta:
            print(f"[bold red]Error: La carpeta '{carpeta}' no es una carpeta[/bold red]")
        elif not os.path.exists(carpeta):
            print(f"[bold red]Error: La carpeta '{carpeta}' no existe[/bold red]")
        else:
            if not ctypes.windll.shell32.IsUserAnAdmin():
                try:
                    shutil.rmtree(carpeta)
                except PermissionError:
                    print(f"[bold red]Error: No tienes permisos para eliminar '{carpeta}', ejecute en modo de administrador[/bold red]")
                except Exception as e:
                    print(f"[bold red]Error al eliminar '{carpeta}': {e}[/bold red]")
            else:
                try:
                    os.system(f"rd /s /q {carpeta}")
                except Exception as e:
                    print(f"[bold red]Error al eliminar '{carpeta}': {e}[/bold red]")
    # codigo para moverse de directorio
    # cd 
    elif request.startswith("cd"):
        new_directory = request[3:].strip()
        if not new_directory:
            print("[bold red]Error: Debes especificar un directorio[/bold red]")
        elif not os.path.exists(new_directory):
            print(f"[bold red]Error: El directorio '{new_directory}' no existe[/bold red]")
        else:
            try:
                os.chdir(new_directory)
                print(f"[bold #FFFF00]Directorio actualizado a '{new_directory}'[/bold #FFFF00]")
                directory = os.getcwd()
            except Exception as e:
                print(f"[bold red]Error al cambiar de directorio: {e}[/bold red]")
    # para entrar en modo administrador
    elif request == "pp-pysh --push-admin":
        resquest_admin = input("Coloque [Y] o [N] para entrar en modo administrador : ").upper()
        if resquest_admin == "Y":
            if not ctypes.windll.shell32.IsUserAnAdmin():
                script = sys.executable
                params = " ".join(sys.argv)
                ctypes.windll.shell32.ShellExecuteW(None, "runas", script, params, None, 1)
                sys.exit()  # Cierra el proceso actual y deja solo el nuevo con permisos
            else:
                print("[bold green]Ya estás en modo administrador.[/bold green]")
        elif resquest_admin == "n":
            print("[bold #FFFF00]se detuvo la operación de entrar en modo de administrador[/bold #FFFF00]")
        else:
            print("[bold red]ERROR : Digito mal para confirmar la operación[bold red]")
    elif request.startswith("pysh --crt-carp"):
        carpeta = request.replace("pysh --crt-carp", "").strip()
        if carpeta:
            with Progress() as progress_create:
                create_carp = progress_create.add_task("[bold #1E90FF]Creando carpeta...", total=100)
                while not progress_create.finished:
                    progress_create.update(create_carp, advance=25)
                    sleep(0.3)
            os.mkdir(carpeta)
            print(f"[bold #FFFF00]Carpeta '{carpeta}' creada exitosamente[/bold #FFFF00]")
        else:
            print("[bold red]Error: Debes especificar un nombre para la carpeta[/bold red]")
    elif request.startswith("pysh --crt-arch"):
        archivo = request.replace("pysh --crt-arch", "").strip()
        if archivo:
            with Progress() as progress_create:
                create_arch = progress_create.add_task("[bold #1E90FF]Creando archivo...", total=100)
                while not progress_create.finished:
                    progress_create.update(create_arch, advance=25)
                    sleep(0.3)
            try:
                with open(archivo, "w") as f:  # Se usa 'open' para crear un archivo
                    pass  # No escribe nada, solo lo crea
                print(f"[bold #FFFF00]Archivo '{archivo}' creado exitosamente[/bold #FFFF00]")
            except Exception as e:
                print(f"[bold red]Error al crear el archivo '{archivo}': {e}[/bold red]")
        else:
            print("[bold red]Error: Debes especificar un nombre para el archivo[/bold red]")
    # exit
    elif request == "pysh -exit" or request == "exit()" or request == "exit":
        progress_bar()
        sys.exit()
    # mensaje de error
    else:
        print("[bold red]Comando no reconocido[/bold red]")

####################################################
# Clear Shell
####################################################
def clearsh():
    os.system("cls")
    inicialisador()

####################################################
# Progress bar
####################################################
def progress_bar():
    with Progress() as progress:
        tarea = progress.add_task("[cyan]saliendo...", total=100)
        
        while not progress.finished:
            progress.update(tarea, advance=20)
            sleep(0.2)

def progress_bar_download():
    with Progress() as progress:
        tarea = progress.add_task("[cyan]verificando descarga...", total=100)
        
        while not progress.finished:
            progress.update(tarea, advance=15)
            sleep(0.5)

def progress_bar_open_editor_code():
    with Progress() as progress:
        tarea = progress.add_task("[cyan]Abriendo el editor de codigo...", total=100)
        
        while not progress.finished:
            progress.update(tarea, advance=25)
            sleep(0.3)

####################################################
# Ejecutor del programa
####################################################
if __name__ == "__main__":
    inicialisador()