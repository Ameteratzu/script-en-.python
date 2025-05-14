import requests

def enviar_sms(api_key, numero, mensaje):
    url = 'https://textbelt.com/text'
    data = {
        'phone': numero,
        'message': mensaje,
        'key': api_key,
    }

    try:
        response = requests.post(url, data=data)
        respuesta_json = response.json()

        if respuesta_json['success']:
            print('SMS enviado correctamente')
        else:
            print(f'Error al enviar SMS: {respuesta_json["error"]}')
    
    except requests.exceptions.RequestException as req_err:
        print(f'Error de solicitud HTTP: {req_err}')
    
    except Exception as e:
        print(f'Error inesperado: {str(e)}')

def main():
    try:
        # Proporciona información directamente
        api_key_textbelt = 'a097cfa9d6b414320baa541d13fd611185ea4f43GAvZncVqizGWPU9Qbb1kN2bAt'  # Reemplaza con tu clave de API real
        numero_destino = '+56 934095462'  # Reemplaza con el número de teléfono de destino real
        mensaje_a_enviar = 'Este es un mensaje de ejemplo.'  # Reemplaza con el mensaje real que deseas enviar

        # Enviar el SMS
        enviar_sms(api_key_textbelt, numero_destino, mensaje_a_enviar)
    
    except KeyboardInterrupt:
        print('\nOperación cancelada por el usuario.')

if __name__ == "__main__":
    main()
