
import pyautogui
import webbrowser as wb
import time

wb.open("web.whatsapp.com")

time.sleep(30)
for i in range(40): #   Loops through fourty times
    pyautogui.write("HEYYOU!") #    Small optimization that, instead of writing "HEYYOU!" one letter at a time, it writes it all at once.
    pyautogui.press("enter")
#scan whatsapp from the appeared window and open the chat where you want to spam. You only have a mere 40 seconds to do so.
