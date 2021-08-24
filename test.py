import win32gui
import win32con
import keyboard
import time
import pywintypes
import win32gui, win32com.client

shell = win32com.client.Dispatch("WScript.Shell")

pseudos = []
hwndd = []

def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        if "Dofus" in win32gui.GetWindowText(hwnd):
            hwndd.append(hwnd)
            pseudos.append(win32gui.GetWindowText(hwnd))

win32gui.EnumWindows(winEnumHandler, None)

account = 0

print("You're accounts :")

for k in range(len(hwndd)):
    print(str(k + 1) + ". " + pseudos[k].split(" ")[0])

rep = str(input("Show the initiative like this - account n°1 account n°2 etc.. : "))

initiative = rep.split(" ")

final_initiative = {initiative.index(r): int(r) for r in initiative}

while True:
    if keyboard.is_pressed('tab'):
        win32gui.ShowWindow(hwndd[final_initiative[account]-1], win32con.SW_SHOWMAXIMIZED)
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(hwndd[final_initiative[account]-1])
        account += 1
        if account >= len(hwndd):
            account = 0
        time.sleep(0.2)
            
