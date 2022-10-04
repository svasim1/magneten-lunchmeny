import os
import requests
import json
import html
import datetime
import tkinter as tk
from tkinter import *
from apscheduler.schedulers.blocking import BlockingScheduler

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def updateLunchMenu():
    date = datetime.datetime.now()
    content = requests.get("https://www.foodandco.se/api/restaurant/menu/week?language=sv&restaurantPageId=188244&weekDate=" + str(date.date()))
    data = json.loads(content.text)

    weekData = data["LunchMenus"][date.weekday()]
    data = "\n\n".join([html.unescape(x.lstrip("\n").lstrip("<p>").lstrip("br />")) for x in weekData["Html"].split("</p>")[:-1]])
    clear()
    print("Dagens Lunchmeny: " + weekData["DayOfWeek"] + "\n+----------------------+\n\n" + data)

updateLunchMenu()

scheduler = BlockingScheduler()
scheduler.add_job(updateLunchMenu, 'interval', hours=3)
scheduler.start()