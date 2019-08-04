from Resources import Resources
from Bot import Bot
import keyboard

# main execution
bot = Bot()
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed("="):
            bot.purchaseLoop()
            print(bot.field)
            print(bot.field.champions)
        else:
            pass
    except:
        print("Oh no.")  # if user pressed other than the given key the loop will break
