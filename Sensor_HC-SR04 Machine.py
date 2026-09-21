import machine  # Importar módulo machine para control de hardware     #Programa de SunFounder modificado por Carlos Lorente Jiménez
import time  # Importar módulo time para retrasos

# Definir números de pines para TRIG y ECHO del sensor ultrasónico
TRIG = machine.Pin(3, machine.Pin.OUT)  # Pin TRIG como salida
ECHO = machine.Pin(4, machine.Pin.IN)  # Pin ECHO como entrada

def distance():
    # Función para calcular distancia en centímetros
    TRIG.low()  # Establecer TRIG en bajo
    time.sleep_us(2)  # Esperar 2 microsegundos
    TRIG.high()  # Establecer TRIG en alto
    time.sleep_us(10)  # Esperar 10 microsegundos
    TRIG.low()  # Establecer TRIG en bajo nuevamente

    # Mientras el pin ECHO tenga valor 0, no hagas nada
    while ECHO.value() == 0:
        pass

    t1 = time.ticks_us()  # Registrar el tiempo (en microsegundos) cuando ECHO se pone en alto

    # Mientras el pin ECHO tenga valor 1, no hagas nada
    while ECHO.value() == 1:
        pass

    t2 = time.ticks_us()  # Registrar el tiempo (en microsegundos) cuando ECHO se pone en bajo

    # Calcular la duración del pin ECHO en alto
    t = t2 - t1

    # Devolver la distancia calculada (usando la velocidad del sonido)
    return t * 340  / (2 * 10000)  # Distancia en centímetros

# Bucle principal
while True:
    dis = distance()  # Obtener distancia del sensor
    print(f"Distance: {dis:.2f} cm") # Imprimir distancia con dos decimales utilizando f-string
    time.sleep_ms(300)  # Esperar 300 milisegundos antes de la siguiente medición