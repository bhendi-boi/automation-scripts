import pyautogui
import time
# update the values of username and password variables with your credentials and
# run this script and open your browser within 5 min to for it to work properly
username: str = ""
password: str = ""
browserNames = ["brave", "google chrome"]

data = {"userName": username, "password": password}


def core() -> bool:
    pyautogui.leftClick(x=500, y=600)
    pyautogui.write("\t")
    time.sleep(2)
    pyautogui.write(data["userName"] + "\t")
    time.sleep(2)
    pyautogui.write(data["password"])
    time.sleep(2)
    pyautogui.press("enter")
    return True


while True:
    fw = pyautogui.getActiveWindow()
    tabName = fw.title.lower()
    flag = False
    for browser in browserNames:
        if browser in tabName:
            flag = core()
    if flag:
        break
    time.sleep(2)
