import webbrowser as web
import pyautogui as pg
import time

numberPhone = '+55XXXXXXXXXXX'

web.open(f"https://web.whatsapp.com/send?phone={numberPhone}")
time.sleep(10)
with open("message.txt", 'r', encoding='utf8') as text:
    for line in text:
        pg.write(line.strip())
        time.sleep(2)
        pg.press('enter')