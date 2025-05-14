# Proyecto de Scripts de Python

Este repositorio contiene una serie de scripts de Python que fueron creados con fines educativos y experimentales. Los scripts están diseñados para demostrar conceptos de automatización, pruebas de seguridad y simulación de bots, entre otros. A continuación, se describen brevemente los scripts incluidos.

## Scripts Incluidos

1. **Regalo de San Valentín.py**
   - **Descripción:** Este script fue diseñado para enviar un mensaje de regalo o felicitación en el día de San Valentín a un contacto de tu elección utilizando automatización en tu escritorio.
   - **Tecnologías utilizadas:** `pyautogui` para la automatización de tareas en el escritorio.
   - **Objetivo:** Practicar la automatización de teclas y mouse para generar un mensaje personalizado.
   - **Nota:** Utiliza la interfaz gráfica de usuario para interactuar con las aplicaciones.

2. **brute force.py**
   - **Descripción:** Este script implementa un ataque de fuerza bruta con el fin de demostrar cómo se pueden probar diferentes combinaciones de contraseñas. 
   - **Advertencia:** Este script es **estrictamente educativo**. No debe utilizarse para fines maliciosos o sin el consentimiento explícito de las partes involucradas.
   - **Objetivo:** Aprender y experimentar con técnicas de seguridad y cómo pueden defenderse las contraseñas de los sistemas.
   - **Precaución:** Su uso en sistemas ajenos sin autorización es **ilegal** y **contraproducente**.

3. **spambot_wha.py**
   - **Descripción:** Este script simula el comportamiento de un bot de spam en WhatsApp. Envía mensajes automáticos a un número o grupo de WhatsApp.
   - **Tecnologías utilizadas:** `pyautogui` para automatizar el envío de mensajes en WhatsApp Web.
   - **Advertencia:** Este script se proporciona **con fines educativos** únicamente. El envío de spam en plataformas sin consentimiento de los usuarios es **ilegal** y **no se recomienda**.
   - **Objetivo:** Demostrar cómo automatizar tareas repetitivas y practicar el uso de bots.

4. **anonimo_sms.py**
   - **Descripción:** Este script permite enviar mensajes SMS de forma anónima utilizando la API de [Textbelt](https://textbelt.com/text). El número del remitente no se muestra, lo que hace el mensaje anónimo.
   - **Tecnologías utilizadas:** `requests` para realizar peticiones HTTP a la API de Textbelt.
   - **Objetivo:** Enviar un SMS de manera anónima para fines educativos. Este script no debe ser utilizado para fines maliciosos o ilegales.
   - **Precaución:** El uso de mensajes anónimos sin consentimiento puede ser considerado como acoso y es ilegal en muchas jurisdicciones.

5. **sms_0.1.py**
   - **Descripción:** Este script permite enviar SMS desde un número virtual utilizando la API de [Textbelt](https://textbelt.com/text). El mensaje puede ser enviado a cualquier número, pero se incluye el número virtual de Textbelt como remitente.
   - **Tecnologías utilizadas:** `requests` para realizar peticiones HTTP a la API de Textbelt.
   - **Objetivo:** Enviar un SMS de manera controlada desde un número virtual para fines educativos.
   - **Precaución:** El uso de este script para realizar actividades no autorizadas, como spam o acoso, es **ilegal** y **no recomendable**.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/scripts-educativos.git

2. Instalar dependencias
   ```bash
   pip install requests pyautogui

3. Para ejecutar cualquier script
   ```bash
   python <nombre_del_script>.py
