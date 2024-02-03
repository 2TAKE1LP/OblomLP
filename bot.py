# -*- coding: utf-8 -*-
# воркает только в чатах, в личках не нихуя
import requests
import vk_api, json, requests, traceback,pathlib 
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import os,re
import vk_captchasolver as vc
from threading import Thread
import sqlite3
import time 
import config
from config import config
import sqlite3

vk = vk_api.VkApi(token=config['general'])
longpoll = VkLongPoll(vk) 

class DotDict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

beggin = False
con = sqlite3.connect(config['base'], check_same_thread=False)
cur = con.cursor()  
answers = {}
try:
 cur.execute("SELECT * FROM `answers`")
 result = cur.fetchall()
 for i in result:
  answers[i[0]] = i[1]
except:
 pass

try:
 cur.execute("SELECT * FROM `settings`")
 result = cur.fetchone()
 if result != None:
  if result[0] != 'no':
   settings = {'prefix': result[0],'status': result[1]}
  else:
   settings = {'prefix': "",'status': result[1]}
 else:
  cur.execute("INSERT INTO `settings`(`prefix`,`status`) VALUES ('no',NULL)")
  con.commit()
  settings = {'prefix': "",'status': None}
except:
 pass

con.close()

def status():
 while True:
  try:
   if settings['status'] != None:
    vk.method("status.set", {"text": settings['status'] + " %s" % str(time.strftime("%H:%M", time.localtime()))}) 
  except Exception as E:
   print(E)
  time.sleep(60)

Thread(target=status, args=[]).start() 

def answer():
 global beggin
 global answers
 global settings

 try:
  id = event.peer_id
  idsms = event.message_id
  try:
   with open(answers[str(ids)],"r") as f:
   	ans = f.read().splitlines()
   try:
    vk.method("messages.send", {"peer_id": id, "message": random.choice(ans), "forward_messages": idsms, "random_id": random.randint(0,99999999)})
   except vk_api.exceptions.Captcha as captcha:
    try:
     sid = captcha.sid # Получение sid
     img_data = requests.get(captcha.get_url()).content
     name = random.randint(0,999999)
     with open('%s.jpg' % name, 'wb') as handler:
      handler.write(img_data)   
     code = vc.solve(image='%s.jpg' % name)
     vk.method("messages.send", {"peer_id": id, "message": random.choice(ans), "forward_messages": idsms, "message_id": int(idsms),  "captcha_sid": sid, "random_id": random.randint(0,99999999)})
     os.remove("%s.jpg" % name)         
    except Exception as E:
     print(E) 
  except:
   pass
  


  if ids != config['owner']:
   pass
  elif message.lower() == "%sтест" % settings['prefix']:
   vk.method("messages.send", {"peer_id": id, "message": "Я работаю!", "random_id": random.randint(0,99999999)})	
  elif "+краш" in message.lower():
   try:
    args1 = int(message.split(" ")[1])
    args2 = int(message.split(" ")[2])      
    
    beggin = True
    for i in range(args1):
     try:
      if beggin == False:
       break
      else:
       try:
        text = "#обломовы Залетели сюда и крошат ваши ебла ™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™™"
        idsms = vk.method("messages.send", {"peer_id": id, "message": ".", "random_id": random.randint(0,99999999)}) 
        vk.method("messages.edit", {"peer_id": id, "message": text, "message_id": int(idsms)})
        time.sleep(args2)
       except vk_api.exceptions.Captcha as captcha:
          try:
           sid = captcha.sid # Получение sid
           img_data = requests.get(captcha.get_url()).content
           name = random.randint(0,999999)
           with open('%s.jpg' % name, 'wb') as handler:
            handler.write(img_data)   
           code = vc.solve(image='%s.jpg' % name)
           vk.method("messages.edit", {"peer_id": id, "message": text, "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
           os.remove("%s.jpg" % name)         
          except Exception as E:
           print(E) 


     except Exception as E: 
      print(E)    
   except Exception as E:
   	print(E)
  elif message.lower() == "stop":
   beggin = False   
   try:
    vk.method("messages.edit", {"peer_id": id, "message": "Остановила", "message_id": int(idsms)})
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       vk.method("messages.edit", {"peer_id": id, "message": "Остановила", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 
  elif message.lower() == "/info":
   beggin = False   
   try:
    vk.method("messages.edit", {"peer_id": id, "message": "Префикс: %s\nСтатус: %s" % (settings['prefix'],settings['status']), "message_id": int(idsms)})
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       vk.method("messages.edit", {"peer_id": id, "message": "Префикс: %s\nСтатус: %s" % (settings['prefix'],settings['status']),  "captcha_sid": sid, "captcha_key": code }) 
       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 
  
  elif "+добавь" in message.lower():
   con = sqlite3.connect(config['base'], check_same_thread=False)
   cur = con.cursor()
   args1 = message.split(" ")[1]
   args2 = message.split(" ")[2] 
   cur.execute("SELECT * FROM `files` WHERE `file`='%s' or `name`='%s'" % (args2,args1))
   if cur.fetchone() != None:
    success = False  
   else:
    try:
     with open(args2,'r') as f:
      text = f.read()
     if len(text) > 0:
      cur.execute("INSERT INTO `files`('file','name') VALUES ('%s','%s')" % (args2,args1)) 
      con.commit()
      success = True
     else:
      success = False
    except:
     success = False


   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})    	
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 
  elif "удали" in message.lower():
   con = sqlite3.connect(config['base'], check_same_thread=False)
   cur = con.cursor()  
   args1 = message.split(" ")[1] 

   cur.execute("SELECT * FROM `files` WHERE `name`='%s'" % args1)
   result = cur.fetchone()
   if result == None:
    success = False  
   else:
    try:
      cur.execute("DELETE FROM `files` WHERE `name`='%s'" % args1) 
      cur.execute("DELETE FROM `answers` WHERE `file`='%s'" % result[1]) 
      con.commit()
      success = True
    except:
     success = False


   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})    	
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 

  elif "+отв" in message.lower():
   con = sqlite3.connect(config['base'], check_same_thread=False)
   cur = con.cursor()   
   args1 = message.split(" ")[1]
   cur.execute("SELECT `file` FROM `files` WHERE `name`='%s'" % args1)
   result = cur.fetchone()
   success = False
   if result != None:
    try:
     json_object = DotDict(event.__dict__)
     idmess = eval(json_object['attachments']['reply'])['conversation_message_id']
     iduser = int(vk.method("messages.getByConversationMessageId", {"peer_id": id, "conversation_message_ids": idmess})['items'][0]['from_id'])
    except:
     try:
      iduser = message.split(" ")[2] 
      if "|" in str(iduser):
       iduser = str(iduser).split("|")[0].replace("[id","")
       iduser = int(iduser)
      elif "vk.com" in str(iduser) or "https://" in str(iduser):
       iduser = str(iduser).replace("https://","").replace("vk.com/","")
       iduser = vk.method("users.get", {"user_ids":iduser, "fields": "id"})
       iduser = int(iduser[0]["id"])
     except Exception as E: 
      print(E)
    iduser = int(iduser)
    cur.execute("SELECT * FROM `answers` WHERE `id_vk`='%s'" % iduser)
    if cur.fetchone() == None:
     cur.execute("INSERT INTO `answers`(`id_vk`,`file`) VALUES ('%s','%s')" % (iduser,result[0]))
     con.commit()
     answers[str(iduser)] = result[0]
     success = True

  
   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})    	
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 

  elif "-отв" in message.lower():
   con = sqlite3.connect(config['base'], check_same_thread=False)
   cur = con.cursor()   
   success = False
   try:
     json_object = DotDict(event.__dict__)
     idmess = eval(json_object['attachments']['reply'])['conversation_message_id']
     iduser = int(vk.method("messages.getByConversationMessageId", {"peer_id": id, "conversation_message_ids": idmess})['items'][0]['from_id'])
   except:
     try:
      iduser = message.split(" ")[1]
      if "|" in str(iduser):
       iduser = str(iduser).split("|")[0].replace("[id","")
       iduser = int(iduser)
      elif "vk.com" in str(iduser) or "https://" in str(iduser):
       iduser = str(iduser).replace("https://","").replace("vk.com/","")
       iduser = vk.method("users.get", {"user_ids":iduser, "fields": "id"})
       iduser = int(iduser[0]["id"])
     except Exception as E: 
      print(E)
   iduser = int(iduser)
   cur.execute("SELECT * FROM `answers` WHERE `id_vk`='%s'" % iduser)
   if cur.fetchone() != None:
    cur.execute("DELETE FROM `answers` WHERE `id_vk`='%s'" % iduser)
    con.commit()
    del answers[str(iduser)]
    success = True

  
   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})    	
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 
  
  elif "+префикс" in message.lower():
   con = sqlite3.connect(config['base'], check_same_thread=False)
   cur = con.cursor()     
   args1 = message.replace("/prefix ","",1)
   success = False

   if args1.lower() == "none":
    cur.execute("UPDATE `settings` SET `prefix`='no'")
    con.commit()
    settings['prefix'] = ""
    success = True
   else:
    cur.execute("UPDATE `settings` SET `prefix`='%s'" % args1)
    con.commit()
    settings['prefix'] = args1
    success = True

   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})      
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 
  elif "-шаблон" in message.lower():
   args1 = message.split(" ")[1]
   success = False
   files = os.listdir()
   for i in files:
    if i == "%s.base" % args1:
     os.remove("%s.base" % args1)
     success = True
     break

   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})      
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 


  elif "тспам+" in message.lower():
   args1 = int(message.split(" ")[1])
   args2 = int(message.split(" ")[2])
   success = False
   try:
     json_object = DotDict(event.__dict__)
     idmess = eval(json_object['attachments']['reply'])['conversation_message_id']
     iduser = int(vk.method("messages.getByConversationMessageId", {"peer_id": id, "conversation_message_ids": idmess})['items'][0]['from_id'])
     args4 = message.split(" ")[3].replace("[","").replace("]","")
   except:
     try:
      iduser = message.split(" ")[3]
      args4 = message.split(" ")[4].replace("[","").replace("]","")
      if "|" in str(iduser):
       iduser = str(iduser).split("|")[0].replace("[id","")
       iduser = int(iduser)
      elif "vk.com" in str(iduser) or "https://" in str(iduser):
       iduser = str(iduser).replace("https://","").replace("vk.com/","")
       iduser = vk.method("users.get", {"user_ids":iduser, "fields": "id"})
       iduser = int(iduser[0]["id"])
     except Exception as E: 
      print(E)
   iduser = int(iduser)
   try:
    with open("%s.base" % args4, encoding='Windows-1251') as f:
     mat = f.read().splitlines()
    beggin = True
    for i in range(args1):
     try:
      if beggin == False:
       break
      else:
       try:
         vk.method("messages.send", {"peer_id": id, "message": "[id%s|%s]" % (iduser,random.choice(mat)), "random_id": random.randint(0,99999999)})
       except vk_api.exceptions.Captcha as captcha:
         try:
          sid = captcha.sid # Получение sid
          img_data = requests.get(captcha.get_url()).content
          name = random.randint(0,999999)
          with open('%s.jpg' % name, 'wb') as handler:
           handler.write(img_data)   
          code = vc.solve(image='%s.jpg' % name)
          vk.method("messages.send", {"peer_id": id, "message": "[id%s|%s]" % (iduser,random.choice(mat)),  "captcha_sid": sid, "captcha_key": code, "random_id": random.randint(0,99999999)})
          os.remove("%s.jpg" % name)          
         except Exception as E:
          print(E) 
     except:
      pass 
     time.sleep(args2)  
    success = True
   except Exception as E:
    print(E)
   

   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})      
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 


  elif "+шаблон" in message.lower():
   args1 = message.split("\n")[0].split(" ")[1]
   args2 = message.split("\n")
   del args2[0]
   files = os.listdir()
   success = False
   for i in files:
    if "%s.base" % args1 == i:
     with open(i,'a') as f:
      for b in args2:
       f.writelines("%s\n" % b)
     success = True
     break
   if success == False:
    f = open("%s.base" % args1,"w")
    f.close()
    with open("%s.base" % args1, "a") as f:
     for i in args2:
      f.writelines("%s\n" % i)
    success = True

   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})      
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 


  elif "+статус" in message.lower():
   con = sqlite3.connect(config['base'], check_same_thread=False)
   cur = con.cursor()  

   args1 = message.replace("+статус ","")
   success = False

   if args1.lower() == "none":
    cur.execute("UPDATE `settings` SET `status`=NULL")
    con.commit()
    settings['status'] = None
    success = True
   else:
    cur.execute("UPDATE `settings` SET `status`='%s'" % args1)
    con.commit()
    settings['status'] = args1
    success = True

   try:
    if success == True:
     vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms)})
    else:
     vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms)})      
   except vk_api.exceptions.Captcha as captcha:
      try:
       sid = captcha.sid # Получение sid
       img_data = requests.get(captcha.get_url()).content
       name = random.randint(0,999999)
       with open('%s.jpg' % name, 'wb') as handler:
        handler.write(img_data)   
       code = vc.solve(image='%s.jpg' % name)
       if success == True:
        vk.method("messages.edit", {"peer_id": id, "message": "Успешно!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 
       else:
        vk.method("messages.edit", {"peer_id": id, "message": "Ошибка!", "message_id": int(idsms),  "captcha_sid": sid, "captcha_key": code }) 

       os.remove("%s.jpg" % name)         
      except Exception as E:
       print(E) 

  elif "+f" in message.lower():
   beggin = True
   args1 = int(message.split(" ")[1])
   args2 = message.split(" ")[2]

   with open(args2, "r") as f:
   	text = f.read().split(" ")
   del text[len(text) - 1]
   try:
    json_object = DotDict(event.__dict__)
    idmess = eval(json_object['attachments']['reply'])['conversation_message_id']
    iduser = int(vk.method("messages.getByConversationMessageId", {"peer_id": id, "conversation_message_ids": idmess})['items'][0]['from_id'])
   except:
    try:
     if len(settings['prefix']) > 0:
      iduser = message.split(" ")[4]
     else:
      iduser = message.split(" ")[3]
     if "|" in str(iduser):
       iduser = str(iduser).split("|")[0].replace("[id","")
       iduser = int(iduser)
     elif "vk.com" in str(iduser) or "https://" in str(iduser):
       iduser = str(iduser).replace("https://","").replace("vk.com/","")
       iduser = vk.method("users.get", {"user_ids":iduser, "fields": "id"})
       iduser = int(iduser[0]["id"])
    except Exception as E: 
     print(E)
   iduser = int(iduser)
   for i in range(args1):    
    for i in text:
     try:
       if beggin == False:
        break
       else:
        try:
         vk.method("messages.send", {"peer_id": id, "message": "[id%s|%s]" % (iduser,i), "random_id": random.randint(0,99999999)})
        except vk_api.exceptions.Captcha as captcha:
         try:
          sid = captcha.sid # Получение sid
          img_data = requests.get(captcha.get_url()).content
          name = random.randint(0,999999)
          with open('%s.jpg' % name, 'wb') as handler:
           handler.write(img_data)   
          code = vc.solve(image='%s.jpg' % name)
          vk.method("messages.send", {"peer_id": id, "message": "[id%s|%s]" % (iduser,i),  "captcha_sid": sid, "captcha_key": code, "random_id": random.randint(0,99999999)})
          os.remove("%s.jpg" % name)    
 
         except Exception as E:
          print(E) 
     except Exception as E:
      print(E)   
 except Exception as E:
  print(E)




while True:
  try:
   for event in longpoll.listen(): 
    if event.type == VkEventType.MESSAGE_NEW:
     if event.from_chat:
      ids = event.user_id
      message = event.text
      #if ids == config['owner']:

      if len(settings['prefix']) > 0:
       if "%s " % str(settings['prefix']).lower() not in message.lower():
         break
       else:
        message = str(message).replace("%s " % settings['prefix'],"",1)
      Thread(target=answer, args=[]).start() 
  except Exception as E:
   print(E)