import pyautogui
import time
# update the values of username and password variables with your credentials and
# open the browser window after you run this script to work it properly
browserNames = ["brave", "google chrome", "edge", "firefox", "safari"]
IP = "172.25.0.1"

username: str = ""
password: str = ""


def core() -> bool:
    pyautogui.leftClick(x=500, y=600)
    pyautogui.write("\t")
    time.sleep(2)
    pyautogui.write(username + "\t")
    time.sleep(2)
    pyautogui.write(password)
    time.sleep(2)
    pyautogui.press("enter")
    return True


if __name__ == "__main__":
    while True:
        fw = pyautogui.getActiveWindow()
        tabName = fw.title.lower()
        flag = False
        for browser in browserNames:
            if browser in tabName and ((IP in tabName) or ("Fortigate :: Login".lower() in tabName)):
                flag = core()
        if flag:
            break
        time.sleep(2)
