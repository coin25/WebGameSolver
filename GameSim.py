import pyautogui
from time import sleep

class ClickImage:
    def click(self, image, delay = 1):
        sleep(delay)
        image_x, image_y = pyautogui.locateCenterOnScreen("Images/" + image)
        pyautogui.click(image_x, image_y)

def fileToNum(filename):
    return int(filename[:1])

def makeBound(fname1, fname2):
    return fileToNum(fname1) * 10 + fileToNum(fname2)

class FindRange:
    possibleDigits = [str(i) + ".PNG" for i in range(1,10)]
    digitLocations = []

    def __init__(self):
        image_x, image_y = pyautogui.locateCenterOnScreen("Images/LeftTop.PNG")
        self.region = pyautogui.screenshot("Capture.png",region=(image_x, image_y, 400, 400))
        for i in self.possibleDigits:
            #Easier for organization and later sorting
            print(i)
            image_x, image_y = pyautogui.center(pyautogui.locate("Images/3.PNG", self.region))
            try:
                for image_coords in pyautogui.locateAll("Images/" + i, self.region):
                    image_x, image_y = pyautogui.center(image_coords)
                    self.digitLocations.append((image_x, image_y, i))
            except:
                pass
        self.digitLocations = sorted(self.digitLocations,key=lambda x: x[0])
        firstBound = makeBound(self.digitLocations[0][2], self.digitLocations[1][2])
        secondBound = makeBound(self.digitLocations[2][2], self.digitLocations[3][2])
        print(self.digitLocations)
        print(firstBound, secondBound)


class Bot:
    def start(self, seconds = 2):
        sleep(seconds)
        test = FindRange()

bot = Bot()
bot.start()
