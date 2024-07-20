import pyautogui
import time
import random
import pywhatkit as kt


kt.sendwhatmsg("contactnumber with country code ",'hi bete this is brian made by your pita ji (Shree man Aayush ji )',00,6,9)
galia = ["aand","b.c.","bakchod","bc","behenchod","bevakoof","bewday","bhadwaa","bhosdaa","bhosdike","bhosdiki","bhosdiwale","charsi","chuchi","chudne","chudwaane",
         "chut","chutia","chutiye","dalaal","dalal","dalle","dalley","gandu","gotte","hagney","haraamjaade","haraamkhor","harami","jhaat","jhaatu","jhat","kuttey",
         "kutti","landy","launda","lode","lulli","lund","m.c.","madarchod","marunga","pilla","pisaab","pisab","pkmkb","porkistan","randy","suar","tatty","ullu",]
count = 1
while count<=50:
    r_str = random.choice(galia)
    pyautogui.typewrite(r_str)
    time.sleep(0.5000)
    pyautogui.press('enter')
    count+=1

