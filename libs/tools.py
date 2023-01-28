import os
import time


def clear_terminal():  # Limpiar la terminal
    """Limpia la terminal en Windows o Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():  # Funcion para tener una pausa en la terminal
    """Hace una pausa en el programa y espera a que el usuario presione enter."""
    # input("Presione Enter para continuar...")
    time.sleep(1)


def increment_number(number):
    number = str(int(number) + 1).zfill(len(number))
    return number
