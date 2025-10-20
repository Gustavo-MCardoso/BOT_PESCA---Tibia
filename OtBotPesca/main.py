import pyautogui
import random

from actions import click_fish, poke_attack, get_loot, use_pokeball, poke_position, check_battle, send_msg, beep, use_fishing_rod




X_FISH = 339
Y_FISH = 90
RGB_FISH = (66,164,50)

MAX_ATTEMPT = 700
attempt = 0


while True:
    fish = pyautogui.pixelMatchesColor(X_FISH, Y_FISH, RGB_FISH)
    if fish:
        click_fish(X_FISH, Y_FISH)
        pyautogui.sleep(1.5)
        poke_attack()
        pyautogui.sleep(1.5)
        get_loot()
        use_pokeball()
        poke_position()
        pyautogui.sleep(3)
        if not check_battle():
            poke_attack()
            if not check_battle():
                send_msg()
                beep()
                #file_name = screenshot()
                #load_img(file_name)
        use_fishing_rod()
        attempt = 0
    if attempt == MAX_ATTEMPT:
        use_fishing_rod()
        attempt = 0