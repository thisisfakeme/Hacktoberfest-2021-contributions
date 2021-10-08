import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(30)
for i in range(40):
    pyautogui.press("H")
    pyautogui.press("E")
    pyautogui.press("Y")
    pyautogui.press("Y")
    pyautogui.press("O")
    pyautogui.press("U")
    pyautogui.press("!")
    pyautogui.press("enter")
#scan whatsapp from the appeared window and open the chat where you want to spam.
