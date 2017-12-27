import pyautogui
from time import sleep

class ClickImage:
    def click(self, image, delay = 1):
        sleep(delay)
        image_x, image_y = pyautogui.locateCenterOnScreen("Images/" + image)
        pyautogui.click(image_x, image_y)

class FindRange:
    possibleDigits = [str(i) + ".PNG" for i in range(1,10)]
    digitLocations = []

    def __init__(self):
        self.region = pyautogui.screenshot(region=())
        for i in self.possibleDigits:
            #Easier for organization and later sorting
            print(i)
            try:
                image_x, image_y = pyautogui.locateCenterOnScreen("Images/" + i)
                self.digitLocations.append((image_x, image_y))
            except:
                pass
        print(self.digitLocations)


class Bot:
    def start(self, seconds = 2):
        sleep(seconds)
        test = FindRange()

bot = Bot()
bot.start(5)
pyautogui.lo