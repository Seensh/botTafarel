import pyautogui
import keyboard
import time


def functionMain():   
    count = 0
    while keyboard.is_pressed('c') == False:

        time.sleep(3)    
        pyautogui.press('end')
        time.sleep(2)
        #CAPTURA POSIÇÃO VOTO
        #TAMANHO PAGINA 75%
        positionCandidato = pyautogui.locateOnScreen('candidato.png')
        if (positionCandidato != None):
            positionCenterCandidato = pyautogui.center(positionCandidato)
            pyautogui.click(positionCenterCandidato.x,positionCenterCandidato.y)

        time.sleep(2)

        positionButton = pyautogui.locateOnScreen('salvar-button.png', grayscale=True,confidence=0.7)
        if (positionButton != None):
            positionCenterButton = pyautogui.center(positionButton)
            pyautogui.click(positionCenterButton.x,positionCenterButton.y)

        time.sleep(4)

        positionNovamente = pyautogui.locateOnScreen('novamente.png', grayscale=True,confidence=0.8)
        if (positionNovamente != None):
            positionCenterNovamente = pyautogui.center(positionNovamente)
            pyautogui.click(positionCenterNovamente.x,positionCenterNovamente.y)
            time.sleep(1)
            pyautogui.moveTo((positionCenterNovamente.x+320),(positionCenterNovamente.y))

        time.sleep(2)
        count += 1 
        salvaLog(count)

def salvaLog(count):
    print('quantidade de votos: ' + str(count))

functionMain()