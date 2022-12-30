import random
from cryptography.fernet import Fernet
from colorama import init, Fore
init(autoreset=True)

# Apartado key #

# Creación de llave -- Esta es una llave unica y se crea una sola vez, comenta o elimina despues de la primer ejecución

"""def crear_llave():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

crear_llave()"""

def cargar_llave():
  file = open("key.key", "rb")
  key = file.read()
  file.close()
  return key

key = cargar_llave()
fer = Fernet(key)

# Fin de key #


# Apartado comandos #

def view():
  with open("passwords.txt", "r") as f:
    for line in f.readlines():
      data = line.rstrip()
      site, name, password = data.split("|")
      print(Fore.RED + "\nSitio:", site, "| Usuario:", name, "| Contraseña:",
           fer.decrypt(password.encode()).decode() + "\n")            

def gen_pwd():
  letras = "abcdefghijklmnopqrstuvwxyz"
  mayusculas = letras.upper()
  numeros = "0123456789"
  simbolos = "!#$%&*()_-=+."

  base = letras + mayusculas + numeros + simbolos
  longitud = 12

  muestra = random.sample(base,longitud)
  pwd = "".join(muestra)
  return pwd
  
def add():
  site = input("\nEscribe el sitio o app que quieres agregar: ")
  name = input("\nEscribe el nombre de usuario o correo a agregar: ")
  password = gen_pwd()

  with open("passwords.txt", "a") as f:
    f.write(site + "|" + name + "|" + fer.encrypt(password.encode()).decode() + "\n")
    print(Fore.BLUE + f"\nLa contraseña generada y guardada para '{name}' en '{site}' es: {password}\n")

# Fin de comandos #

while True:
  modo = input("""Bienvenido al gestor de contraseñas\n\n
  Menú de comandos:\n\n
  v = ver contraseñas guardadas:
  a = añadir nueva contraseña
  s = salir\n:""").lower()

  if modo == "s":
    break

  if modo == "v":
    view()

  elif modo == "a":
    add()

  else:
    print("comando incorrecto.")
    continue