import pyautogui
import time

if __name__ == "__main__":
    # imagine your laptop screen is a 2-D plane with origin at top left corner
    # and positive x axis is the top border and positive y axis is left border of
    # you screen choose a location on your desktop which donot have clickable items
    # in it and set x, y as coordinates of that locaion w.r.t the plane described
    # above and choose screenOffTime as your laptop screen off time
    x: int = 0
    y: int = 0
    screenOffTime: int = 5
    while True:
        pyautogui.click(x, y)
        print("clicked")
        time.sleep((screenOffTime * 60) - 5)
