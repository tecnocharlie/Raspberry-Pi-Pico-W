#buzzer pasivo sonando melodia de prueba
#Carlos Lorente Jiménez (con asistencia de Gemini IA)
from picozero import Speaker
from time import sleep

# Zumbador pasivo conectado a GP28
speaker = Speaker(28)

# Definimos una melodía de 6 notas utilizando una lista melodia = []
# cada elemento de la lista es una tupla: ('nota', duracion)
# nota (en notación anglosajona y con comillas simple) y duracion (en segundos) 
melodia = [
    ('c4', 0.25),  # Do
    ('d4', 0.25),  # Re
    ('e4', 0.25),  # Mi
    ('f4', 0.25),  # Fa
    ('g4', 0.25),  # Sol
    ('a4', 0.5)    # La (nota final más larga)
]
#se indica en la pantalla de Thonny (consola) que se empieza a reproducir la melodía
print("Reproduciendo melodía...")

# Bucle que extrae el valor de cada tupla de la lista melodia []
# se reproduce nota según duración desde la primera tupla hasta llegar al final
for nota, duracion in melodia:
    
    speaker.play(nota, duracion)
    sleep(0.05) # Breve silencio opcional para separar las notas
    
#se indica en la pantalla de Thonny (consola) que se ha temrinado la melodía y el programa
print("¡Melodía finalizada!")