import requests

def enviar_sms(api_key, numero, mensaje):
    """
    Envía un SMS utilizando la API de Textbelt.

    Parameters:
        - api_key (str): Clave de API de Textbelt.
        - numero (str): Número de teléfono de destino.
        - mensaje (str): Mensaje a enviar.

    Returns:
        None
    """
    url = 'https://textbelt.com/text'
    data = {
        'phone': numero,
        'message': mensaje,
        'key': api_key,
    }

    try:
        # Realizar la solicitud HTTP
        response = requests.post(url, data=data)
        respuesta_json = response.json()

        # Verificar el resultado de la solicitud
        if respuesta_json['success']:
            print('SMS enviado correctamente')
        else:
            print(f'Error al enviar SMS: {respuesta_json["error"]}')
    
    except requests.exceptions.RequestException as req_err:
        print(f'Error de solicitud HTTP: {req_err}')
    
    except Exception as e:
        print(f'Error inesperado: {str(e)}')

def obtener_informacion_envio():
    """
    Solicita al usuario la información necesaria para enviar un SMS.

    Returns:
        Tuple[str, str, str]: Clave de API, Número de teléfono y Mensaje.
    """
    api_key = '880e2babe3965a26935b5cd0a63e82a81e8b76cbZ7bLVyCRo1JsXTkzW9ZK6KjOo'
    numero_destino = input('Introduce el número de teléfono de destino (+1234567890): ')
    mensaje = input('Introduce el mensaje que deseas enviar: ')

    return api_key, numero_destino, mensaje

def main():
    try:
        # Obtener información del usuario
        api_key_textbelt, numero_destino, mensaje_a_enviar = obtener_informacion_envio()

        # Enviar el SMS
        enviar_sms(api_key_textbelt, numero_destino, mensaje_a_enviar)
    
    except KeyboardInterrupt:
        print('\nOperación cancelada por el usuario.')

if __name__ == "__main__":
    main()
