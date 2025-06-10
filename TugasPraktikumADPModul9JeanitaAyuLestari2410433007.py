import os 
import time 
from termcolor import cprint, colored

os.system('cls')
cprint("""
_________________________
|                       |
|         |*\           |
|         |**\          |
|         |***\         |
|         |****\        |
|         |****/        |
|         |***/         |
|         |**/          |
|         |*/           |
|_______________________|
""", "white", "on_red") # anggap aja aplikasi video

n = "Memuat aplikasi Video"
for i in range(10):
    loading = '.' * (i % 4) 
    cprint(f"\r{n}{loading}🌦️    ", "cyan", end="")
    time.sleep(0.7)
os.system("cls")

cprint("""
_________________________
|                       |
|         |*\           |
|         |**\          |
|         |***\         |
|         |****\        |
|         |****/        |
|         |***/         |
|         |**/          |
|         |*/           |
|_______________________|
""", "white", "on_red")

print("DONE!")
time.sleep(0.3)
cprint("Aplikasi Video telah terbuka🥳", "magenta")