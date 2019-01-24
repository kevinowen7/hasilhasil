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
    return {
        "speech": "",
        "messages": [
          {
            "type": 4,
            "payload": {
              "line": {
                  "type": "imagemap",
                  "baseUrl": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/pilih_tanggal%2F12.png?alt=media&_ignore=",
                  "altText": "Pilih Tanggal",
                  "baseSize": {
                    "width": 1040,
                    "height": 1040
                  },
                  "actions": [
                    {
                      "type": "message",
                      "area": {
                        "x": 898,
                        "y": 192,
                        "width": 110,
                        "height": 97
                      },
                      "text": "-"+tipeCari+" "+cari+" 01/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 37,
                        "y": 285,
                        "width": 108,
                        "height": 97
                      },
                      "text": "-"+tipeCari+" "+cari+" 02/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 181,
                        "y": 275,
                        "width": 111,
                        "height": 115
                      },
                      "text": "-"+tipeCari+" "+cari+" 03/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 329,
                        "y": 275,
                        "width": 110,
                        "height": 115
                      },
                      "text": "-"+tipeCari+" "+cari+" 04/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 469,
                        "y": 272,
                        "width": 112,
                        "height": 115
                      },
                      "text": "-"+tipeCari+" "+cari+" 05/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 613,
                        "y": 277,
                        "width": 121,
                        "height": 110
                      },
                      "text": "-"+tipeCari+" "+cari+" 06/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 750,
                        "y": 267,
                        "width": 119,
                        "height": 120
                      },
                      "text": "-"+tipeCari+" "+cari+" 07/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 890,
                        "y": 289,
                        "width": 115,
                        "height": 96
                      },
                      "text": "-"+tipeCari+" "+cari+" 08/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 37,
                        "y": 385,
                        "width": 108,
                        "height": 105
                      },
                      "text": "-"+tipeCari+" "+cari+" 09/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 177,
                        "y": 393,
                        "width": 115,
                        "height": 103
                      },
                      "text": "-"+tipeCari+" "+cari+" 10/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 328,
                        "y": 397,
                        "width": 108,
                        "height": 96
                      },
                      "text": "-"+tipeCari+" "+cari+" 11/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 468,
                        "y": 393,
                        "width": 114,
                        "height": 102
                      },
                      "text": "-"+tipeCari+" "+cari+" 12/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 609,
                        "y": 392,
                        "width": 125,
                        "height": 101
                      },
                      "text": "-"+tipeCari+" "+cari+" 13/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 751,
                        "y": 392,
                        "width": 117,
                        "height": 103
                      },
                      "text": "-"+tipeCari+" "+cari+" 14/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 891,
                        "y": 392,
                        "width": 114,
                        "height": 101
                      },
                      "text": "-"+tipeCari+" "+cari+" 15/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 34,
                        "y": 493,
                        "width": 113,
                        "height": 105
                      },
                      "text": "-"+tipeCari+" "+cari+" 16/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 172,
                        "y": 501,
                        "width": 122,
                        "height": 97
                      },
                      "text": "-"+tipeCari+" "+cari+" 17/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 328,
                        "y": 496,
                        "width": 108,
                        "height": 105
                      },
                      "text": "-"+tipeCari+" "+cari+" 18/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 466,
                        "y": 498,
                        "width": 115,
                        "height": 101
                      },
                      "text": "-"+tipeCari+" "+cari+" 19/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 611,
                        "y": 496,
                        "width": 123,
                        "height": 105
                      },
                      "text": "-"+tipeCari+" "+cari+" 20/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 748,
                        "y": 500,
                        "width": 123,
                        "height": 103
                      },
                      "text": "-"+tipeCari+" "+cari+" 21/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 890,
                        "y": 500,
                        "width": 126,
                        "height": 104
                      },
                      "text": "-"+tipeCari+" "+cari+" 22/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 32,
                        "y": 601,
                        "width": 120,
                        "height": 103
                      },
                      "text": "-"+tipeCari+" "+cari+" 23/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 174,
                        "y": 603,
                        "width": 118,
                        "height": 108
                      },
                      "text": "-"+tipeCari+" "+cari+" 24/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 322,
                        "y": 609,
                        "width": 110,
                        "height": 95
                      },
                      "text": "-"+tipeCari+" "+cari+" 25/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 466,
                        "y": 609,
                        "width": 108,
                        "height": 100
                      },
                      "text": "-"+tipeCari+" "+cari+" 26/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 609,
                        "y": 611,
                        "width": 124,
                        "height": 96
                      },
                      "text": "-"+tipeCari+" "+cari+" 27/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 753,
                        "y": 606,
                        "width": 118,
                        "height": 108
                      },
                      "text": "-"+tipeCari+" "+cari+" 28/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 895,
                        "y": 616,
                        "width": 120,
                        "height": 98
                      },
                      "text": "-"+tipeCari+" "+cari+" 29/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 29,
                        "y": 711,
                        "width": 121,
                        "height": 101
                      },
                      "text": "-"+tipeCari+" "+cari+" 30/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 174,
                        "y": 718,
                        "width": 120,
                        "height": 101
                      },
                      "text": "-"+tipeCari+" "+cari+" 31/"+bulan+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 203,
                        "y": 839,
                        "width": 137,
                        "height": 149
                      },
                      "text": "-"+tipeCari+" "+cari+" -/"+str(int(bulan)-1)+"/"+tahun
                    },
                    {
                      "type": "message",
                      "area": {
                        "x": 721,
                        "y": 832,
                        "width": 121,
                        "height": 147
                      },
                      "text": "-"+tipeCari+" "+cari+" -/"+str(int(bulan)+1)+"/"+tahun
                    }
                  ]
                }
            }
          }
        ]
    }

def flexMessageCari(date,metode):
    #from cari
    return {
      "speech": "",
      "messages": [
        {
          "type": 4,
          "payload": {
              "line": {
                "type": "flex",
                "altText": "Cari Roster Ruangan",
                "contents": {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Froster_judul.png?alt=media&_ignore=",
                    "align": "center",
                    "size": "5xl",
                    "aspectRatio": "2:1"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                      {
                        "type": "separator",
                        "margin": "none",
                        "color": "#994848"
                      },
                      {
                        "type": "image",
                        "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Fjadwal_menu.png?alt=media&_ignore=",
                        "margin": "none",
                        "align": "start",
                        "gravity": "top",
                        "size": "md",
                        "aspectRatio": "2:1",
                        "action": {
                          "type": "message",
                          "label": "menu jadwalku",
                          "text": "menu jadwalku"
                        }
                      },
                      {
                        "type": "text",
                        "text": "Tanggal : "+date,
                        "margin": "lg",
                        "size": "lg",
                        "align": "center",
                        "gravity": "bottom",
                        "weight": "bold",
                        "color": "#191970"
                      },
                      {
                        "type": "image",
                        "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Fpilih_tanggal.png?alt=media&_ignore=",
                        "margin": "none",
                        "align": "center",
                        "gravity": "top",
                        "size": "xxl",
                        "aspectRatio": "2:1",
                        "action": {
                          "type": "message",
                          "label": "pilih tanggal",
                          "text": "pilih tanggal"
                        }
                      },
                      {
                        "type": "text",
                        "text": metode,
                        "margin": "lg",
                        "size": "lg",
                        "align": "center",
                        "gravity": "bottom",
                        "weight": "bold",
                        "color": "#191970"
                      },
                      {
                        "type": "image",
                        "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Fpilih_metode_pencarian.png?alt=media&_ignore=",
                        "margin": "none",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "xxl",
                        "aspectRatio": "2:1",
                        "backgroundColor": "#A1E5E4",
                        "action": {
                          "type": "message",
                          "label": "pilih metode pencari",
                          "text": "pilih metode pencarian"
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Fcari.png?alt=media&_ignore=",
                        "margin": "xxl",
                        "align": "end",
                        "size": "lg",
                        "aspectRatio": "16:9",
                        "action": {
                          "type": "message",
                          "label": "cari",
                          "text": "cari roster"
                        }
                      }
                    ]
                  },
                  "styles": {
                    "hero": {
                      "backgroundColor": "#A1E5E4"
                    },
                    "body": {
                      "backgroundColor": "#A1E5E4"
                    }
                  }
                }
              }
            }

        }
      ]
    }

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

def flexMessageHasilCari(r,date,metode):
    return {
        "speech": "",
       "messages": [
       {
          "type": 4,
          "payload": {
              "line": {
                "type": "flex",
                "altText": "Cari Roster Ruangan",
                "contents": {
                  "type": "bubble",
                  "direction": "ltr",
                  "hero": {
                    "type": "image",
                    "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Froster_judul.png?alt=media&_ignore=",
                    "align": "center",
                    "size": "5xl",
                    "aspectRatio": "2:1"
                  },
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "md",
                    "contents": [
                      {
                        "type": "separator",
                        "margin": "none",
                        "color": "#994848"
                      },
                      {
                        "type": "image",
                        "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Fjadwal_menu.png?alt=media&_ignore=",
                        "margin": "none",
                        "align": "start",
                        "gravity": "top",
                        "size": "md",
                        "aspectRatio": "2:1",
                        "action": {
                          "type": "message",
                          "label": "jadwalku",
                          "text": "jadwalku"
                        }
                      },
                      {
                        "type": "text",
                        "text": date,
                        "margin": "lg",
                        "size": "lg",
                        "align": "center",
                        "gravity": "bottom",
                        "weight": "bold",
                        "color": "#191970"
                      },
                      {
                        "type": "image",
                        "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Fpilih_tanggal.png?alt=media&_ignore=",
                        "margin": "none",
                        "align": "center",
                        "gravity": "top",
                        "size": "xxl",
                        "aspectRatio": "2:1",
                        "action": {
                          "type": "message",
                          "label": "pilih tanggal",
                          "text": "pilih tanggal"
                        }
                      },
                      {
                        "type": "text",
                        "text": metode,
                        "margin": "lg",
                        "size": "lg",
                        "align": "center",
                        "gravity": "bottom",
                        "weight": "bold",
                        "color": "#191970"
                      },
                      {
                        "type": "image",
                        "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Fpilih_metode_pencarian.png?alt=media&_ignore=",
                        "margin": "none",
                        "align": "center",
                        "gravity": "bottom",
                        "size": "xxl",
                        "aspectRatio": "2:1",
                        "backgroundColor": "#8CE4EE",
                        "action": {
                          "type": "message",
                          "label": "pilih metode pencari",
                          "text": "pilih metode pencarian"
                        }
                      },
                      {
                        "type": "image",
                        "url": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/cari_roster_ruangan%2Fcari.png?alt=media&_ignore=",
                        "margin": "xxl",
                        "align": "end",
                        "size": "lg",
                        "aspectRatio": "16:9",
                        "action": {
                          "type": "message",
                          "label": "cari",
                          "text": "cari roster"
                        }
                      }
                    ]
                  },
                  "styles": {
                    "hero": {
                      "backgroundColor": "#a1e6e4"
                    },
                    "body": {
                      "backgroundColor": "#a1e6e4"
                    }
                  }
                }
              }
            }
         },
         {
          "type": 4,
          "payload": {
             "line": {
                "type": "flex",
                "altText": "Hasil Pencarian Rster Ruangan",
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
    
    #untuk menu cari roster
    if req.get("result").get("action") == "menuCariRoster":
        result = req.get("result").get("resolvedQuery")
        if result.lower()=="cari roster":
            metode = userp.child("searchD").get()
            date = userp.child("searchDateR").get()
            
            #jika belum memilih tanggal dan metode pencarian
            if (date==None and metode==None):
                return flexMessageHasilCari("Tolong Masukan Tanggal dan Metodenya kak","Tanggal : -","Metode : -")
            elif (date==None):
                return flexMessageHasilCari("Tolong Masukan Tanggalnya kak","Tanggal : -",metode)
            elif (metode==None):
                return flexMessageHasilCari("Tolong Masukan Metodenya kak",date,"Metode : -")
            
            #proses
            metodeList = metode.split(" : ")
            metodeK = metodeList[0]
            #jika dicari berdasarkan ruangan
            if metodeK == "Ruangan":
                ruang = metode.split("Ruangan : ")[1]
                
                thn = int(date.split("/")[2])
                bln = int(date.split("/")[1])
                tgl = int(date.split("/")[0])

                database = db.reference()
                hasil = database.child(str(thn)+"/"+str(bln)+"/"+str(tgl)).get()
                if hasil==None:
                    return {
                        "speech": "Ruangan "+ruang+" tidak ada jadwal hari ini",
                        "displayText": "Ruangan "+ruang+" tidak ada jadwal hari ini",
                        #"data": {},
                        #"contextOut": [],
                        "source": "Ruangan "+ruang+" tidak ada jadwal hari ini"
                    }

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
                    return {
                        "speech": "Ruangan "+ruang+" tidak ada jadwal hari ini",
                        "displayText": "Ruangan "+ruang+" tidak ada jadwal hari ini",
                        #"data": {},
                        #"contextOut": [],
                        "source": "Ruangan "+ruang+" tidak ada jadwal hari ini"
                    }
                r=""
                for i in hasillist:
                    r=r+i
                #output    
                return flexMessageHasil(r)
            
            #jika dicari berdarkan nama dosen
            if metodeK == "Dosen":
                dosen = metode.split("Dosen : ")[1]
                
                
            
            #jika di cari berdasarkan lantai
            if metodeK=="Lantai":
                lt = metode.split("Lantai : ")[1]
                
                database = db.reference()
                thn = int(date.split("/")[2])
                bln = int(date.split("/")[1])
                tgl = int(date.split("/")[0])
                
                x=1
                hasillist=[]
                hasil = database.child(str(thn)+"/"+str(bln)+"/"+str(tgl)+"/lantai:"+str(lt)).get()
                if hasil==None:
                    return {
                        "speech": "lantai "+str(lt)+" tidak ada jadwal hari ini",
                        "displayText": "lantai "+str(lt)+" tidak ada jadwal hari ini",
                        #"data": {},
                        #"contextOut": [],
                        "source": "lantai "+str(lt)+" tidak ada jadwal hari ini"
                    }
                while(x<len(hasil)):
                    print(hasil[x])
                    if hasil[x]["Nama Dosen"]==" ":
                        hasillist.append("Jam: "+hasil[x]["Jam"]+"\n"+"Mata Kuliah: "+hasil[x]["Mata Kuliah"]+"\n"+"Ruangan: "+hasil[x]["Ruang"]+"\n"+"\n"+"\n")
                    else:
                        hasillist.append("Jam: "+hasil[x]["Jam"]+"\n"+"Mata Kuliah: "+hasil[x]["Mata Kuliah"]+"\n"+"Nama Dosen: "+hasil[x]["Nama Dosen"]+"\n"+"Ruangan: "+hasil[x]["Ruang"]+"\n"+"\n"+"\n")

                    x=x+1
                print(len(hasillist))
                if len(hasillist)==0:
                    return {
                        "speech": "lantai "+str(lt)+" tidak ada jadwal hari ini",
                        "displayText": "lantai "+str(lt)+" tidak ada jadwal hari ini",
                        #"data": {},
                        #"contextOut": [],
                        "source": "lantai "+str(lt)+" tidak ada jadwal hari ini"
                    }
                r=""
                for i in hasillist:
                    r=r+i
                #output    
                return flexMessageHasil(r)
        else:
            date = userp.child("searchDateR").get()
            metode = userp.child("searchD").get()
            #jika datenya blom ada
            if date==None:
                date="-"
            if metode==None:
                metode="Metode : -"
            hasil = flexMessageCari(date,metode)
            return hasil
        
    #untuk input metode dosen
    if req.get("result").get("action") == "inputDosen":
        result = req.get("result").get("resolvedQuery")

        dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
        thn = dateNow.split("-")[0]
        bln = dateNow.split("-")[1]
        tgl = dateNow.split("-")[2]

        hasil = database.child(str(thn)+"/"+str(bln)+"/"+str(tgl)).get()
        if hasil==None:
            return {
                "speech": dosen+" tidak ada jadwal hari ini",
                "displayText": dosen+" tidak ada jadwal hari ini",
                #"data": {},
                #"contextOut": [],
                "source": dosen+" tidak ada jadwal hari ini"
            }
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
            return {
                "speech": dosen+" tidak ada jadwal hari ini",
                "displayText": dosen+" tidak ada jadwal hari ini",
                #"data": {},
                #"contextOut": [],
                "source": dosen+" tidak ada jadwal hari ini"
            }
        r=""
        for i in hasillist:
            r=r+i
        #output    
        return flexMessageHasil(r)
        
    #untuk input metode ruangan
    if req.get("result").get("action") == "inputRuangan": 
        result = req.get("result").get("resolvedQuery")

        dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
        tahun = dateNow.split("-")[0]
        bulan = dateNow.split("-")[1]
        return flexMessageHari(bulan,tahun,"R",result)
            
            
    
    #untuk input lantai
    if req.get("result").get("action") == "inputLantai": 
        try:
            result = req.get("result").get("resolvedQuery")
            if result=="-SETL":
                #return flex message pilih lantai
                return 	{
                  "speech": "",
                  "messages": [
                    {
                      "type": 4,
                      "payload": {
                            "line" : {
                              "type": "imagemap",
                              "baseUrl": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/pilih_lantai%2FPilih%20Lantai.png?alt=media&_ignore=",
                              "altText": "Pilih Lantai",
                              "baseSize": {
                                "width": 1040,
                                "height": 1040
                              },
                              "actions": [
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 2,
                                    "y": 219,
                                    "width": 1031,
                                    "height": 166
                                  },
                                  "text": "-SETL 1"
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 0,
                                    "y": 390,
                                    "width": 1040,
                                    "height": 160
                                  },
                                  "text": "-SETL 2"
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 2,
                                    "y": 550,
                                    "width": 1038,
                                    "height": 163
                                  },
                                  "text": "-SETL 3"
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 0,
                                    "y": 714,
                                    "width": 1035,
                                    "height": 160
                                  },
                                  "text": "-SETL 4"
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 0,
                                    "y": 874,
                                    "width": 1040,
                                    "height": 166
                                  },
                                  "text": "-SETL 5"
                                }
                              ]
                            }
                        }
                    }
                ]
            }	
            else:
                lantai = result.split(" ")[1]
                if ((int(lantai)<=5) and (int(lantai)>=1)):
                    #push to firebase
                    userp.update({
                        "name" : profile.display_name,
                        "searchD" : "Lantai : "+str(int(lantai))
                    })
                    date = userp.child("searchDateR").get()
                    #jika datenya blom ada
                    if date==None:
                        date="-"
                    hasil = flexMessageCari(date,"Lantai : "+str(int(lantai)))
                    return hasil
                else:
                    return {
                        "speech": "Maaf kak , masukan lantai antara 1 sampai 5",
                        "displayText": "Maaf kak , masukan lantai antara 1 sampai 5",
                        #"data": {},
                        #"contextOut": [],
                        "source": "Maaf kak , masukan lantai antara 1 sampai 5"
                    }
        except Exception as res:
            return  {
                "speech": "Maaf kak format lantai yang di input salah :(",
                "displayText": "Maaf kak format lantai yang di input salah :(",
                #"data": {},
                #"contextOut": [],
                "source": "Maaf kak format lantai yang di input salah :("
            }
        
        
    #untuk input tanggal
    if req.get("result").get("action") == "inputTanggal": 
        try:
            result = req.get("result").get("resolvedQuery")
            # jika diminta roster besok
            if result.split("-H ")[1].lower()=="besok":
                dateNow = str(datetime.datetime.now()+ timedelta(days=1,hours=7)).split(" ")[0]
                tahun = dateNow.split("-")[0]
                bulan = dateNow.split("-")[1]
                hari = dateNow.split("-")[2]
            # jika diminta roster hari ini
            elif result.split("-H ")[1].lower()=="hari ini":
                dateNow = str(datetime.datetime.now()+ timedelta(hours=7)).split(" ")[0]
                tahun = dateNow.split("-")[0]
                bulan = dateNow.split("-")[1]
                hari = dateNow.split("-")[2]
            # jika diminta flex untuk input tanggal
            else:
                date = result.split(" ")[1].split("/")
                tahun = date[2]
                bulan = date[1]
                hari = date[0]

                #menampilkan flex message untuk pilih tahun
                if tahun =="-":
                    #from -H -/-/-
                    return {
                    "speech": "",
                    "messages": [
                      {
                        "type": 4,
                        "payload": {
                          "line": {
                            "type": "imagemap",
                            "baseUrl": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/pilih_tanggal%2Fpilih_tahun.png?alt=media&_ignore=",
                            "altText": "Pilih Tahun",
                            "baseSize": {
                              "width": 1040,
                              "height": 1040
                            },
                            "actions": [
                              {
                                "type": "message",
                                "area": {
                                  "x": 290,
                                  "y": 159,
                                  "width": 461,
                                  "height": 214
                                },
                                "text": "-H "+hari+"/"+bulan+"/2018"
                              },
                              {
                                "type": "message",
                                "area": {
                                  "x": 292,
                                  "y": 427,
                                  "width": 459,
                                  "height": 206
                                },
                                "text": "-H "+hari+"/"+bulan+"/2019"
                              },
                              {
                                "type": "message",
                                "area": {
                                  "x": 292,
                                  "y": 679,
                                  "width": 459,
                                  "height": 116
                                },
                                "text": "-H hari ini"
                              },
                              {
                                "type": "message",
                                "area": {
                                  "x": 290,
                                  "y": 812,
                                  "width": 461,
                                  "height": 100
                                },
                                "text": "-H besok"
                              }
                            ]
                          }
                        }
                      }
                    ]
                   }
                #menampilkan flex message untuk pilih bulan
                if bulan =="-":
                    return {
                    "speech": "",
                    "messages": [
                      {
                        "type": 4,
                        "payload": {
                          "line": {
                              "type": "imagemap",
                              "baseUrl": "https://firebasestorage.googleapis.com/v0/b/minabot-aceess.appspot.com/o/pilih_tanggal%2Fpilih_bulan.jpg?alt=media&_ignore=",
                              "altText": "Pilih Bulan",
                              "baseSize": {
                                "width": 1040,
                                "height": 1040
                              },
                              "actions": [
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 15,
                                    "y": 188,
                                    "width": 326,
                                    "height": 130
                                  },
                                  "text": "-H "+hari+"/01/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 361,
                                    "y": 187,
                                    "width": 318,
                                    "height": 132
                                  },
                                  "text": "-H "+hari+"/02/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 704,
                                    "y": 187,
                                    "width": 317,
                                    "height": 129
                                  },
                                  "text": "-H "+hari+"/03/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 17,
                                    "y": 365,
                                    "width": 316,
                                    "height": 130
                                  },
                                  "text": "-H "+hari+"/04/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 360,
                                    "y": 368,
                                    "width": 320,
                                    "height": 123
                                  },
                                  "text": "-H "+hari+"/05/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 704,
                                    "y": 366,
                                    "width": 319,
                                    "height": 127
                                  },
                                  "text": "-H "+hari+"/06/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 19,
                                    "y": 544,
                                    "width": 319,
                                    "height": 133
                                  },
                                  "text": "-H "+hari+"/07/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 361,
                                    "y": 547,
                                    "width": 318,
                                    "height": 127
                                  },
                                  "text": "-H "+hari+"/08/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 702,
                                    "y": 549,
                                    "width": 321,
                                    "height": 128
                                  },
                                  "text": "-H "+hari+"/09/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 25,
                                    "y": 726,
                                    "width": 314,
                                    "height": 127
                                  },
                                  "text": "-H "+hari+"/10/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 363,
                                    "y": 724,
                                    "width": 317,
                                    "height": 127
                                  },
                                  "text": "-H "+hari+"/11/"+tahun
                                },
                                {
                                  "type": "message",
                                  "area": {
                                    "x": 707,
                                    "y": 723,
                                    "width": 314,
                                    "height": 128
                                  },
                                  "text": "-H "+hari+"/12/"+tahun
                                }
                              ]
                            }
                        }
                      }
                    ]
                   }

                #menampilkan flex message untuk pilih hari
                if hari=="-":
                    if (int(bulan)<=12 and int(bulan)>=1):
                        hasil = flexMessageHari(bulan,tahun)
                        return hasil
                    else:
                        return  {
                            "speech": "Maaf kak, format bulan yang anda masukan tidak ada",
                            "displayText": "Maaf kak, format bulan yang anda masukan tidak ada",
                            #"data": {},
                            #"contextOut": [],
                            "source": "Maaf kak, format bulan yang anda masukan tidak ada"
                        }


            #menambahakan data tanggal ke firebase
            if ((hari!="-") and (bulan !="-") and (tahun !="-")):
                #push to firebase
                userp.update({
                    "name" : profile.display_name,
                    "searchDateR" : str(hari)+"/"+str(bulan)+"/"+str(tahun)
                })
                #validasi tanggal
                if ((int(hari)<=31) and (int(hari)>=1) and (int(bulan)>=1) and (int(bulan)<=12)):
                    date = str(hari)+"/"+str(bulan)+"/"+str(tahun)
                    metode = userp.child("searchD").get()
                    #jika metode blom ada
                    if metode==None:
                        metode="Metode : -"
                    hasil = flexMessageCari(date,metode)
                    return hasil
                else:
                    return  {
                        "speech": "Maaf kak format tanggal yang di input salah",
                        "displayText": "Maaf kak format tanggal yang di input salah",
                        #"data": {},
                        #"contextOut": [],
                        "source": "Maaf kak format tanggal yang di input salah"
                    }
                    
        except Exception as res:
            return  {
                "speech": "Maaf kak format tanggal yang di input salah :(",
                "displayText": "Maaf kak format tanggal yang di input salah :(",
                #"data": {},
                #"contextOut": [],
                "source": "Maaf kak format tanggal yang di input salah :("
            }        
############################################################### JADWALKU ##########            
    if req.get("result").get("action") == "jadwalku":
        result0 = req.get("result")
        result = result0.get("resolvedQuery")
        hariKe = result.split(" ")[1]
        if ((int(hariKe)<7) and (int(hariKe)>0)):
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
            #jika tidak ada hasil
            if hasil==None:
                return flexMessageHasil("Hari "+str(cekHari)+" ("+str(hari)+"/"+str(bulan)+"/"+str(tahun)+") tidak ada jadwal")
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
        else:
            return flexMessageHasil("Format hari jadwalku yang anda masukan harus di antara 1 - 6")
        
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
