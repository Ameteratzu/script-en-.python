import random
import difflib

def generar_contraseñas_similares(palabra_clave, longitud_min, longitud_max, limite):
    character = "0123456789abcdefghijklmnopqrstuvwxyz.,-"
    character_list = list(character)
    
    # Ruta completa del archivo
    archivo_resultados = "C:\\Users\\hp\\Desktop\\kali\\contraseñas_similares.txt"

    # Abre el archivo en modo escritura, creándolo si no existe
    with open(archivo_resultados, "w") as archivo:
        for _ in range(limite):
            # Generar una longitud aleatoria entre longitud_min y longitud_max
            longitud_generada = random.randint(longitud_min, longitud_max)
            
            contraseña_similar = ''.join(random.choice(character_list) if random.random() < 0.7 else c for c in palabra_clave)
            
            # Asegurarse de que la contraseña generada tenga la longitud deseada
            contraseña_similar = contraseña_similar[:longitud_generada]
            
            # Evaluar similitud con difflib
            similitud = difflib.SequenceMatcher(None, palabra_clave, contraseña_similar).ratio()
            
            # Guardar solo contraseñas similares por encima de un umbral (puedes ajustar este umbral según tus necesidades)
            umbral_similitud = 0.5
            if similitud > umbral_similitud:
                archivo.write(f"{contraseña_similar}\n")

# Pedir al usuario que ingrese una palabra clave
palabra_clave_ingresada = input("Ingresa una palabra clave: ")

# Establecer el límite de contraseñas a generar
limite_contraseñas = 1000000

# Llamar a la función para generar contraseñas similares y guardarlas
generar_contraseñas_similares(palabra_clave_ingresada, 4, 10, limite_contraseñas)

print(f"Contraseñas similares generadas y guardadas en 'contraseñas_similares.txt'.")
