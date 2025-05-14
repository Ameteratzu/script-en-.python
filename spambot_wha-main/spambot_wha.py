import pywhatkit as kit
import time

# Número de teléfono al que deseas enviar los mensajes
numero_telefono = "+51 922 155 704"  # Reemplaza con el número real, incluyendo el código de país

# Mensaje que deseas enviar
mensaje = "-------------------- --------------"

# Número de veces que deseas enviar el mensaje
cantidad_mensajes = 10

# Espera de 5 segundos antes de comenzar a enviar
time.sleep(5)

for i in range(cantidad_mensajes):
    kit.sendwhatmsg_instantly(numero_telefono, mensaje, wait_time=10)
    # Espera entre cada mensaje
    time.sleep(2)
