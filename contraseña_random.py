
import random
import string

def generar_contraseña_aleatoria(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def elegir_longitud():
    longitud = int(input("Ingrese la cantidad de caracteres que desea que contenga la contraseña: "))
    return longitud

def main():
    longitud = elegir_longitud()
    contraseña_aleatoria = generar_contraseña_aleatoria(longitud)
    print("Contraseña generada:", contraseña_aleatoria)

if __name__ == "__main__":
    main()