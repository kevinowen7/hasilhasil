#!/usr/bin/env python


import json
import os
import requests
import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth

from flask import Flask
from flask import request
from flask import make_response

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


# firebase
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://minabot-aceess.firebaseio.com/'
})

line_bot_api = LineBotApi('tRo0KibnDeYJgRVUj01Nnh0+MSCTUhbyZo0HgSwtfRZzGt5Gh0kZUUuiDJkOswWWWsQulRJylBl3seFXcWr10Zu2SJldz8Qxd5sdBxxEQa2k374wJdd1vcNQVrGOusGnFErAt4SPvq4FhZLUdN1vEgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0d184e88d0b01d9a5586b06abd6a1250')


# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])


def webhook():
    req = request.get_json()
    res = makeWebhookResult(req)  
    
    res = json.dumps(res, indent=4)
    
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    
    return r

def flexMessageHari(bulan,tahun,tipeCari,cari):
    bulan=str(int(bulan))
    tahun=str(int(tahun))
    
    #hari ini
    dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
    tahunNow = dateNow.split("-")[0]
    bulanNow = dateNow.split("-")[1]
    hariNow = dateNow.split("-")[2]
    
    # next date
    nextDate = str(datetime.date(int(tahun),int(bulan),int(15))+ timedelta(days=30)).split("-")
    tahunNext = nextDate[0]
    bulanNext = nextDate[1]
    hariNext = nextDate[2]
    
    # prev date
    prevDate = str(datetime.date(int(tahun),int(bulan),int(15))- timedelta(days=30)).split("-")
    tahunPrev = prevDate[0]
    bulanPrev = prevDate[1]
    hariPrev = prevDate[2]
    ##
    
    t = bulan
    if (bulan=="2"):
        if int(tahun)%4==0:
            t="29"
    url = "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/calender%2F_"+t+"_.png?alt=media&_ignore="
    data = {
        "speech": "",
        "messages": [
          {
            "type": 4,
            "payload": {
              "line": {
                "type": "imagemap",
                "baseUrl": url,
                "altText": "Pilih Tanggal",
                "baseSize": {
                    "width": 1040,
                    "height": 940
                },
                "actions": [
                    {
                    "type": "message",
                    "area": {
                        "x": 31,
                        "y": 26,
                        "width": 193,
                        "height": 168
                    },
                    "text": "-"+tipeCari+" "+cari+" -/"+bulanPrev+"/"+tahunPrev
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 251,
                        "y": 20,
                        "width": 532,
                        "height": 178
                    },
                    "text": "bulan"
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 816,
                        "y": 20,
                        "width": 191,
                        "height": 174
                    },
                    "text": "-"+tipeCari+" "+cari+" -/"+bulanNext+"/"+tahunNext
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 47,
                        "y": 263,
                        "width": 106,
                        "height": 92
                    },
                    "text": "-"+tipeCari+" "+cari+" 01/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 155,
                        "y": 263,
                        "width": 114,
                        "height": 94
                    },
                    "text": "-"+tipeCari+" "+cari+" 02/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 269,
                        "y": 265,
                        "width": 108,
                        "height": 92
                    },
                    "text": "-"+tipeCari+" "+cari+" 03/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 377,
                        "y": 261,
                        "width": 117,
                        "height": 98
                    },
                    "text": "-"+tipeCari+" "+cari+" 04/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 494,
                        "y": 257,
                        "width": 132,
                        "height": 100
                    },
                    "text": "-"+tipeCari+" "+cari+" 05/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 626,
                        "y": 259,
                        "width": 114,
                        "height": 100
                    },
                    "text": "-"+tipeCari+" "+cari+" 06/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 740,
                        "y": 255,
                        "width": 121,
                        "height": 104
                    },
                    "text": "-"+tipeCari+" "+cari+" 07/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 861,
                        "y": 261,
                        "width": 132,
                        "height": 102
                    },
                    "text": "-"+tipeCari+" "+cari+" 08/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 55,
                        "y": 357,
                        "width": 94,
                        "height": 96
                    },
                    "text": "-"+tipeCari+" "+cari+" 09/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 153,
                        "y": 357,
                        "width": 116,
                        "height": 100
                    },
                    "text": "-"+tipeCari+" "+cari+" 10/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 269,
                        "y": 357,
                        "width": 108,
                        "height": 102
                    },
                    "text": "-"+tipeCari+" "+cari+" 11/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 377,
                        "y": 359,
                        "width": 110,
                        "height": 102
                    },
                    "text": "-"+tipeCari+" "+cari+" 12/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 487,
                        "y": 359,
                        "width": 123,
                        "height": 102
                    },
                    "text": "-"+tipeCari+" "+cari+" 13/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 610,
                        "y": 359,
                        "width": 122,
                        "height": 102
                    },
                    "text": "-"+tipeCari+" "+cari+" 14/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 732,
                        "y": 359,
                        "width": 126,
                        "height": 100
                    },
                    "text": "-"+tipeCari+" "+cari+" 15/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 858,
                        "y": 363,
                        "width": 135,
                        "height": 96
                    },
                    "text": "-"+tipeCari+" "+cari+" 16/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 55,
                        "y": 457,
                        "width": 100,
                        "height": 94
                    },
                    "text": "-"+tipeCari+" "+cari+" 17/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 163,
                        "y": 459,
                        "width": 108,
                        "height": 87
                    },
                    "text": "-"+tipeCari+" "+cari+" 18/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 279,
                        "y": 459,
                        "width": 98,
                        "height": 88
                    },
                    "text": "-"+tipeCari+" "+cari+" 19/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 377,
                        "y": 461,
                        "width": 117,
                        "height": 90
                    },
                    "text": "-"+tipeCari+" "+cari+" 20/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 494,
                        "y": 463,
                        "width": 126,
                        "height": 86
                    },
                    "text": "-"+tipeCari+" "+cari+" 21/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 620,
                        "y": 461,
                        "width": 122,
                        "height": 84
                    },
                    "text": "-"+tipeCari+" "+cari+" 22/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 742,
                        "y": 459,
                        "width": 123,
                        "height": 86
                    },
                    "text": "-"+tipeCari+" "+cari+" 23/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 865,
                        "y": 459,
                        "width": 128,
                        "height": 89
                    },
                    "text": "-"+tipeCari+" "+cari+" 24/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 57,
                        "y": 551,
                        "width": 106,
                        "height": 91
                    },
                    "text": "-"+tipeCari+" "+cari+" 25/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 167,
                        "y": 549,
                        "width": 106,
                        "height": 97
                    },
                    "text": "-"+tipeCari+" "+cari+" 26/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 273,
                        "y": 549,
                        "width": 104,
                        "height": 97
                    },
                    "text": "-"+tipeCari+" "+cari+" 27/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 377,
                        "y": 551,
                        "width": 123,
                        "height": 95
                    },
                    "text": "-"+tipeCari+" "+cari+" 28/"+bulan+"/"+tahun
                    },
                    {
                    "type": "message",
                    "area": {
                        "x": 26,
                        "y": 734,
                        "width": 988,
                        "height": 175
                    },
                    "text": "-"+tipeCari+" "+cari+" "+hariNow+"/"+bulanNow+"/"+tahunNow
                    }
                ]
                }
            }
          }
        ]
    }
    if (bulan=="2"):
        if int(tahun)%4==0:
            totalHari="29"
            data["messages"][0]["payload"]["line"]["actions"].append({
                "type": "message",
                "area": {
                    "x": 500,
                    "y": 549,
                    "width": 124,
                    "height": 95
                },
                "text": "-"+tipeCari+" "+cari+" 29/"+bulan+"/"+tahun
                })
        else:
            totalHari="28"
    elif (bulan=="1") or (bulan=="3") or (bulan=="5") or (bulan=="7") or (bulan=="8") or (bulan=="10") or (bulan=="12"):
        totalHari="31"
        data["messages"][0]["payload"]["line"]["actions"].append({
            "type": "message",
            "area": {
                "x": 500,
                "y": 549,
                "width": 124,
                "height": 95
            },
            "text": "-"+tipeCari+" "+cari+" 29/"+bulan+"/"+tahun
            })
        data["messages"][0]["payload"]["line"]["actions"].append({
            "type": "message",
            "area": {
                "x": 624,
                "y": 546,
                "width": 124,
                "height": 100
            },
            "text": "-"+tipeCari+" "+cari+" 30/"+bulan+"/"+tahun
            })
        data["messages"][0]["payload"]["line"]["actions"].append({                                                        
            "type": "message",
            "area": {
                "x": 748,
                "y": 547,
                "width": 117,
                "height": 99
            },
            "text": "-"+tipeCari+" "+cari+" 31/"+bulan+"/"+tahun
            })
    else:
        totalHari="30"  
        data["messages"][0]["payload"]["line"]["actions"].append({
            "type": "message",
            "area": {
                "x": 500,
                "y": 549,
                "width": 124,
                "height": 95
            },
            "text": "-"+tipeCari+" "+cari+" 29/"+bulan+"/"+tahun
            })
        data["messages"][0]["payload"]["line"]["actions"].append({
            "type": "message",
            "area": {
                "x": 624,
                "y": 546,
                "width": 124,
                "height": 100
            },
            "text": "-"+tipeCari+" "+cari+" 30/"+bulan+"/"+tahun
            })
    return data

def flexMessageHasil(r):
    return {
        "speech": "",
       "messages": [
        {
          "type": 4,
          "payload": {
             "line": {
                "type": "flex",
                "altText": "Hasil Pencarian Roster Ruangan",
                "contents": {
                 "type": "bubble",
                  "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": r,
                        "wrap": True
                      }
                    ]
                  }
                 }
             }
          }
       }
     ]
    }


def makeWebhookResult(req):  
    #push user id to firebase
    userid = req.get("originalRequest").get("data").get("source").get("userId")
    profile = line_bot_api.get_profile(userid)
    database = db.reference()
    userp = database.child("user").child(userid)
    userp.update({
        "name" : profile.display_name
    })
    
        
    #untuk input metode dosen
    if req.get("result").get("action") == "inputDosen":
        dosen = req.get("result").get("resolvedQuery")

        dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
        thn = int(dateNow.split("-")[0])
        bln = int(dateNow.split("-")[1])
        tgl = int(dateNow.split("-")[2])
        #untuk proses roster dari lantai dan ruangan
        hasil = database.child(str(thn)+"/"+str(bln)+"/"+str(tgl)).get()
        if hasil==None:
            return flexMessageHasil(dosen+" tidak ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+")")
        lt=1
        hasillist=[]
        while(lt<len(hasil)+1):
            x=1
            try:
                while(x<len(hasil["lantai:"+str(lt)])):
                    if(dosen.lower() in hasil["lantai:"+str(lt)][x]["Nama Dosen"].lower()) or (dosen.lower() in hasil["lantai:"+str(lt)][x]["Mata Kuliah"].lower()):
                        if hasil["lantai:"+str(lt)][x]["Nama Dosen"]==" ":
                            hasillist.append("Jam: "+hasil["lantai:"+str(lt)][x]["Jam"]+"\n"+"Mata Kuliah: "+hasil["lantai:"+str(lt)][x]["Mata Kuliah"]+"\n"+"Ruangan: "+hasil["lantai:"+str(lt)][x]["Ruang"]+"\n"+"\n"+"\n")                
                        else:
                            hasillist.append("Jam: "+hasil["lantai:"+str(lt)][x]["Jam"]+"\n"+"Mata Kuliah: "+hasil["lantai:"+str(lt)][x]["Mata Kuliah"]+"\n"+"Nama Dosen: "+hasil["lantai:"+str(lt)][x]["Nama Dosen"]+"\n"+"Ruangan: "+hasil["lantai:"+str(lt)][x]["Ruang"]+"\n"+"\n"+"\n")
                    print(hasil["lantai:"+str(lt)][x]["Nama Dosen"])
                    x=x+1
                lt=lt+1
            except Exception as res:
                lt=lt+1
        if len(hasillist)==0:
            return flexMessageHasil(dosen+" tidak ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+")")
        r=""
        for i in hasillist:
            r=r+i
        #output    
        return flexMessageHasil(dosen+" ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+") \n\n"+r)
        
            
            
    
    #untuk input lantai
    if req.get("result").get("action") == "inputLantai": 
        try:
            dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
            tahun = dateNow.split("-")[0]
            bulan = dateNow.split("-")[1]
            lantai = req.get("result").get("resolvedQuery").split("-SETL")[1]
            if ((int(lantai)<=5) and (int(lantai)>=1)):
                return flexMessageHari(bulan,tahun,"SETL",str(lantai))
            else:
                return flexMessageHasil("Maaf kak , masukan lantai antara 1 sampai 5")
        except Exception as res:
            return flexMessageHasil("Maaf kak format lantai yang di input salah :(")
    
    #untuk proses roster dari lantai dan ruangan
    if req.get("result").get("action") == "lantairuangan":
        result = req.get("result").get("resolvedQuery")
        #jika ruangan yang akan di proses
        if result.split(" ")[0]=="-SETR":
            ruang = result.split(" ")[1].split("/")[1]
            lt = result.split(" ")[1].split("/")[0]
            try:
                if ((int(lt)<=5) and (int(lt)>=1)):
                    print("masuk")
                else:
                    #jika lantai yang di masukan salah
                    return flexMessageHasil("Maaf kak , masukan lantai antara 1 sampai 5")
            except Exception as res:
                return flexMessageHasil("Maaf kak , Format lantai yang dimasukan salah")

            #jika belum memilih ruangan
            if (ruang=="-"):
               hasil = database.child("dataJSON/lantai"+str(lt)).get()
               return hasil
            
            #jika belum memilih tanggal
            try:
                date = result.split(" ")[2]
            except Exception as res:
                dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
                tahun = int(dateNow.split("-")[0])
                bulan = int(dateNow.split("-")[1])
                return flexMessageHari(str(bulan),str(tahun),"SETR",str(lt)+"/"+str(ruang))
            
            #jika sudah memilih tanggal
            try:
                thn = int(date.split("/")[2])
                bln = int(date.split("/")[1])
            except Exception as res: 
                return flexMessageHasil("Format tanggal yang dimasukan salah kak")
            
            try:
                tgl = int(date.split("/")[0])
            except Exception as res:   
                #jika belum memilih hari dan validasi
                if (bln>0) and (bln<13):
                    return flexMessageHari(str(bln),str(thn),"SETR",str(lt)+"/"+str(ruang))
                else:
                    return flexMessageHasil("Format tanggal yang dimasukan salah kak")
            
            hasil = database.child(str(thn)+"/"+str(bln)+"/"+str(tgl)).get()
            if hasil==None:
                return flexMessageHasil("Ruangan "+str(ruang)+" tidak ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+")")
            ruang = ruang.replace("_"," ")
            lt=1
            hasillist=[]
            while(lt<len(hasil)+1):
                x=1
                try:
                    while(x<len(hasil["lantai:"+str(lt)])):
                        if(ruang.lower() in hasil["lantai:"+str(lt)][x]["Ruang"].lower()):
                            if hasil["lantai:"+str(lt)][x]["Nama Dosen"]==" ":
                                hasillist.append("Jam: "+hasil["lantai:"+str(lt)][x]["Jam"]+"\n"+"Mata Kuliah: "+hasil["lantai:"+str(lt)][x]["Mata Kuliah"]+"\n"+"Ruangan: "+hasil["lantai:"+str(lt)][x]["Ruang"]+"\n"+"\n"+"\n")                
                            else:
                                hasillist.append("Jam: "+hasil["lantai:"+str(lt)][x]["Jam"]+"\n"+"Mata Kuliah: "+hasil["lantai:"+str(lt)][x]["Mata Kuliah"]+"\n"+"Nama Dosen: "+hasil["lantai:"+str(lt)][x]["Nama Dosen"]+"\n"+"Ruangan: "+hasil["lantai:"+str(lt)][x]["Ruang"]+"\n"+"\n"+"\n")
                        print(hasil["lantai:"+str(lt)][x]["Nama Dosen"])
                        x=x+1
                    lt=lt+1
                except Exception as res:
                    lt=lt+1

            if len(hasillist)==0:
                return flexMessageHasil("Ruangan "+str(ruang)+" tidak ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+")")
            r=""
            for i in hasillist:
                r=r+i
            #output    
            return flexMessageHasil("Ruangan "+str(ruang)+" ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+") \n\n"+r)
            
        #jika lantai yang akan di proses
        if result.split(" ")[0]=="-SETL":
            lt = result.split(" ")[1]
            try:
                if ((int(lt)<=5) and (int(lt)>=1)):
                    print("masuk")
                else:
                    #jika lantai yang di masukan salah
                    return flexMessageHasil("Maaf kak , masukan lantai antara 1 sampai 5")
            except Exception as res:
                return flexMessageHasil("Maaf kak , Format lantai yang dimasukan salah")
            
            #jika belum memilih tanggal
            try:
                date = result.split(" ")[2]
            except Exception as res:
                dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
                tahun = dateNow.split("-")[0]
                bulan = dateNow.split("-")[1]
                return flexMessageHari(bulan,tahun,"SETL",str(lt))
            
            #jika sudah memilih tanggal
            try:
                thn = int(date.split("/")[2])
                bln = int(date.split("/")[1])
            except Exception as res: 
                return flexMessageHari("Format tanggal yang dimasukan salah kak")
            
            try:
                tgl = int(date.split("/")[0])
            except Exception as res:   
                #jika belum memilih hari dan validasi
                if (bln>0) and (bln<13):
                    return flexMessageHari(str(bln),str(thn),"SETL",str(lt))
                else:
                    return flexMessageHari("Format tanggal yang dimasukan salah kak")
            
            x=1
            hasillist=[]
            hasil = database.child(str(thn)+"/"+str(bln)+"/"+str(tgl)+"/lantai:"+str(lt)).get()
            if hasil==None:
                return flexMessageHasil("lantai "+str(lt)+" tidak ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+")")
            while(x<len(hasil)):
                print(hasil[x])
                if hasil[x]["Nama Dosen"]==" ":
                    hasillist.append("Jam: "+hasil[x]["Jam"]+"\n"+"Mata Kuliah: "+hasil[x]["Mata Kuliah"]+"\n"+"Ruangan: "+hasil[x]["Ruang"]+"\n"+"\n"+"\n")
                else:
                    hasillist.append("Jam: "+hasil[x]["Jam"]+"\n"+"Mata Kuliah: "+hasil[x]["Mata Kuliah"]+"\n"+"Nama Dosen: "+hasil[x]["Nama Dosen"]+"\n"+"Ruangan: "+hasil[x]["Ruang"]+"\n"+"\n"+"\n")

                x=x+1
            print(len(hasillist))
            if len(hasillist)==0:
                return flexMessageHasil("lantai "+str(lt)+" tidak ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+")")
            r=""
            for i in hasillist:
                r=r+i
            #output    
            return flexMessageHasil("lantai "+str(lt)+" ada jadwal ("+str(tgl)+"/"+str(bln)+"/"+str(thn)+") \n\n"+r)
            
############################################################### JADWALKU ##########            
    if req.get("result").get("action") == "jadwalku":
        result0 = req.get("result")
        result = result0.get("resolvedQuery")
        hariKe = result.split(" ")[1]
        if (hariKe=="today"):
            database = db.reference()
            user = database.child("user")
            x=1
            hasillist=[]

            #time
            dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
            time = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[1]
            tahun = int(dateNow.split("-")[0])
            bulan = int(dateNow.split("-")[1])
            hari = int(dateNow.split("-")[2])
            hasil = database.child(str(tahun)+"/"+str(bulan)+"/"+str(hari)).get()
            cekHari = "ini"
            
        elif ((int(hariKe)<7) and (int(hariKe)>0)):
            #next monday
            namaHari=["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu"]
            w=[]
            today = datetime.datetime.now()+ timedelta(hours=7)
            selisih_today_monday = str(datetime.timedelta(days=-today.weekday(), weeks=1)).split(" ")[0]
            next_monday = today + datetime.timedelta(days=-today.weekday(), weeks=1)
            todayS = str(today).split(" ")[0]
            # today
            today_hari = int(todayS.split("-")[2])
            today_bulan = int(todayS.split("-")[1])
            today_tahun = int(todayS.split("-")[0])
            selisih = 6-int(selisih_today_monday)

            x=0
            #monday ke selisih_today_monday
            while x<=int(selisih):
                w.append(str(next_monday + datetime.timedelta(days=x)).split(" ")[0])
                x=x+1
            #today ke monday
            x=0
            while x<int(selisih_today_monday)-1:
                w.append(str(today + datetime.timedelta(days=x)).split(" ")[0])
                x=x+1

            #cek hari
            cekHari = namaHari[int(hariKe)-1]
            dateAkhir = w[int(hariKe)-1]


            #proses
            x=1
            hasillist=[]
            hari = int(dateAkhir.split("-")[2])
            bulan = int(dateAkhir.split("-")[1])
            tahun = int(dateAkhir.split("-")[0])
            hasil = database.child(str(tahun)+"/"+str(bulan)+"/"+str(hari)).get()
        else:
            return flexMessageHasil("Format hari jadwalku yang anda masukan harus di antara 1 - 6")
        
        #return value
        #jika tidak ada hasil
        if hasil==None:
            return flexMessageHasil("Kak "+str(name)+" hari "+str(cekHari)+" ("+str(hari)+"/"+str(bulan)+"/"+str(tahun)+") tidak ada jadwal")
        matkul = userp.child("matkul").get()
        #name
        name = userp.child("name").get()
        #jika tidak ada matkul yang terdaftar
        if matkul==None:
            return flexMessageHasil("Maaf kak "+str(name)+" anda belum mendaftarkan Mata kuliah, silahkan daftarkan mata kuliah anda")
        matkul1 = matkul.split("\n")
        for i in matkul1:
            lt=1
            while (lt<=5):
                x=1
                try:
                    while(x<len(hasil["lantai:"+str(lt)])):
                        if (hasil["lantai:"+str(lt)][x]["Mata Kuliah"]).lower() == i.lower():
                            if hasil["lantai:"+str(lt)][x]["Nama Dosen"]==" ":
                                hasillist.append("Jam: "+hasil["lantai:"+str(lt)][x]["Jam"]+"\n"+"Mata Kuliah: "+hasil["lantai:"+str(lt)][x]["Mata Kuliah"]+"\n"+"Ruangan: "+hasil["lantai:"+str(lt)][x]["Ruang"]+"\n"+"\n"+"\n")
                            else:
                                hasillist.append("Jam: "+hasil["lantai:"+str(lt)][x]["Jam"]+"\n"+"Mata Kuliah: "+hasil["lantai:"+str(lt)][x]["Mata Kuliah"]+"\n"+"Nama Dosen: "+hasil["lantai:"+str(lt)][x]["Nama Dosen"]+"\n"+"Ruangan: "+hasil["lantai:"+str(lt)][x]["Ruang"]+"\n"+"\n"+"\n")

                        x=x+1
                    print("    ")
                    print("    ")
                    print(len(hasillist))
                    lt=lt+1
                # jika ltnya loncat langsung lt 2 dst
                except Exception as res:
                    lt=lt+1

        if hasillist==[]:
            return flexMessageHasil("Hari "+str(cekHari)+" ("+str(hari)+"/"+str(bulan)+"/"+str(tahun)+") \n"+str(name)+" tidak ada kelas")
        else:
            name = userp.child("name").get()
            r=""
            for i in hasillist:
                r=r+i
            hasillist=[]
            return flexMessageHasil("Jadwal kak "+str(name)+" \nHari "+str(cekHari)+" ("+str(hari)+"/"+str(bulan)+"/"+str(tahun)+") : " +"\n"+"\n"+r)

    # menambah matkul    
    if req.get("result").get("action") == "add":
        matkul = userp.child("matkul").get()
        if matkul == None:
            matkul = ""
        result0 = req.get("result")
        result = result0.get("resolvedQuery")
        #validasi
        result1=list(result)

        if ((len(result1) != 6) or (result1[2] != "-")):
            return  {
                "speech": "Maaf kak mungkin kode kuliah yang anda masukan salah :((",
                "displayText": "Maaf kak mungkin kode kuliah yang anda masukan salah :((",
                #"data": {},
                #"contextOut": [],
                "source": "Maaf kak mungkin kode kuliah yang anda masukan salah :(("
            }
        else:
            matkul=matkul+result+"\n"
            #push to firebase
            userp.update({
                "name" : profile.display_name,
                "matkul" : matkul
            })
            
        return {
            "speech": "Sukses menambahkan "+result,
            "displayText": "Sukses menambahkan "+result,
            #"data": {},
            #"contextOut": [],
            "source": "Sukses menambahkan "+result
        }
            
    
    #falback
    if req.get("result").get("action") == "falback":
        return {
            "speech": "Maaf kak Mina belum terlalu mengerti , mohon gunakan fitur menu yang sudah tersedia dulu",
            "displayText": "Maaf kak Mina belum terlalu mengerti , mohon gunakan fitur menu yang sudah tersedia dulu",
            #"data": {},
            #"contextOut": [],
            "source": "line"
        }
        
        
if __name__ == '__main__':
    port = int(os.getenv('PORT', 4040))

    print ("Starting app on port %d" %(port))

    app.run(debug=False, port=port, host='0.0.0.0')
