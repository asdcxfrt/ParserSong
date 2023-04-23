from bs4 import BeautifulSoup
import time
import requests
from lxml import etree
import arrow
import traceback

url = "https://goood.pw/music/requests"
sxpath="""//*[@id="__next"]/div/main/div/div[2]/div/a"""
namexpath = """//*[@id="__next"]/div/main/div/div[2]/div/a/div[2]/div[1]"""




def GetINFO():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    dom = etree.HTML(str(soup))
    utc = arrow.utcnow().shift(hours=+5)
    return [dom.xpath(sxpath)[0].get('href'),dom.xpath(namexpath)[0].text, utc.format('YYYY-MM-DD HH:mm:ss')]

songURL=""

while True:
    try:
        INFO=GetINFO()
        if(songURL!=INFO[0]):
            songURL=INFO[0]
            with open("ListSongs","a",encoding="utf-8") as f:
                f.write(f"{INFO[2]} | {songURL} | {INFO[1]}\n")
        time.sleep(5)
    except Exception as e:
        utc = arrow.utcnow().shift(hours=+5)
        with open("Log.Log","a",encoding="utf-8") as f:
            f.write(f"Время ошибки: {utc.format('YYYY-MM-DD HH:mm:ss')}\n {traceback.format_exc()}") 
        time.sleep(10)



