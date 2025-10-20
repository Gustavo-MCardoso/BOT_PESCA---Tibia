import pyautogui
import random
import winsound
from datetime import datetime

X_TILE = 574
Y_TILE = 373
RGB_TILE = (45,81,72)


POKE_DEAD_POSITION = (643,377)
LOOT_POSITION = (1191, 502)


LIST_ATTACK = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
LIST_OCEAN_POSITION = [(533, 246), (773, 278), (535, 269)]
LIST_MSG = ['Sua Net ta boa?', 'eae?', 'nao dropa TM nunca', 'que lag horrivel', 'opa', 'slv', 'So minha net que ta zuada assim?']

BATTLE_REGION = (979, 113, 176, 96)

USE_POKEBALL = True

def check_battle():
    battle = pyautogui.locateOnScreen('battle.PNG', confidence=0.8, region= BATTLE_REGION)
    if battle is not None:
        return True
    return False

def send_msg():
    msg= random.choice(LIST_MSG)
    pyautogui.write(msg)
    pyautogui.press('enter')

def beep():
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)

#def screenshot():
    now = datetime.now().strftime('%d-%m-%Y-%H-%M')
    file_name = now + '.PNG'
    pyautogui.screenshot(file_name)
    return file_name


def click_fish(x_fish, y_fish):
    pyautogui.moveTo(x_fish, y_fish)
    pyautogui.click()


def poke_attack():
    pyautogui.press(LIST_ATTACK)


def get_loot():
    pyautogui.moveTo(POKE_DEAD_POSITION)
    pyautogui.click(button='right')
    pyautogui.sleep(1)
    pyautogui.moveTo(LOOT_POSITION)
    pyautogui.click(clicks=5, )


def use_pokeball():
    if USE_POKEBALL:
        pyautogui.moveTo(POKE_DEAD_POSITION)
        pyautogui.press('capslock')
        pyautogui.sleep(0.8)
        pyautogui.click() 


def poke_position():
    poke = pyautogui.pixelMatchesColor(X_TILE, Y_TILE, RGB_TILE)
    if not poke:
        pyautogui.press('f11')
        pyautogui.moveTo(X_TILE, Y_TILE)
        pyautogui.click()          
    

def use_fishing_rod():
    ocean_position = random.choice(LIST_OCEAN_POSITION)
    pyautogui.press('f12')
    pyautogui.moveTo(ocean_position)
    pyautogui.click()     