import pyautogui
from time import sleep

class ClickImage:
    def click(self, image, delay = 1):
        sleep(delay)
        image_x, image_y = pyautogui.center(pyautogui.locateOnScreen("Images/" + image))
        pyautogui.click(image_x, image_y)


class Bot:
    def start(self, seconds = 2):
        sleep(seconds)

