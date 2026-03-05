import pyautogui
import keyboard
import threading
import time
import sys  # Necesario para cerrar el programa

# Variable global para controlar el estado del autoclicker
autoclicker_activo = False

# Función que controla el scroll
def autoclicker_scroll():
    while True:
        if autoclicker_activo:
            pyautogui.scroll(10)  # Desplaza hacia arriba


        time.sleep(0.01)  # Intervalo de 0.1 segundos entre desplazamientos

# Función que maneja el cambio de estado cuando se pulsan las teclas
def manejar_teclas():
    global autoclicker_activo
    while True:
        if keyboard.is_pressed('4'):  # Activa el autoclicker
            autoclicker_activo = True
            print("Autoclicker activado")
            time.sleep(0.3)  # Para evitar múltiples activaciones rápidas

        if keyboard.is_pressed('5'):  # Desactiva el autoclicker
            autoclicker_activo = False
            print("Autoclicker desactivado")
            time.sleep(0.3)  # Para evitar múltiples desactivaciones rápidas

        if keyboard.is_pressed('6'):  # Cierra el programa
            print("Cerrando programa...")
            time.sleep(0.3)
            sys.exit()  # Cierra el programa de forma segura

# Crear y lanzar el hilo para manejar el autoclicker
hilo_autoclicker = threading.Thread(target=autoclicker_scroll)
hilo_autoclicker.daemon = True
hilo_autoclicker.start()

# Iniciar la función que escucha las teclas
manejar_teclas()
