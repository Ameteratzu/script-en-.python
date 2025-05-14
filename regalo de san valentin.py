import pyautogui as pg
import pyperclip as pyc
import time

emojis='🥰😘😻💌💘💝💖💗💓💞❣️❤️‍🔥❤️‍🩹❤️💜💑👩‍❤️‍👨👨‍❤️‍👨👩‍❤️‍👩🏩'

def dibujar_corazon(e):
    c = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0],
        [0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        ]
    corazon = "[U+200E]"
    
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] == 1:
                corazon += e
            else:
                corazon += '    '
        corazon += '\n'

    pyc.copy(corazon)


mensajes = int(input('Número de mensajes: '))
time.sleep(3)

for i in range(mensajes):
    dibujar_corazon(emojis[i%10])
    pg.hotkey('ctrl','v')
    pg.press('enter')