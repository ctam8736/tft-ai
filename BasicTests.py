from Resources import Resources
from Bot import Bot
import keyboard

# main execution
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed("="):
            bot = Bot()
            bot.purchaseLoop()
        else:
            pass
    except:
        print("Oh no.")  # if user pressed other than the given key the loop will break
