import os
import json
import random
import time 
import requests
import battles
global link
link = "https://jumnji-server.oredgaming.repl.co/"

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def header(text, clsOn=True):
  if clsOn:
    cls()
  print("===|"+text+"|===")

def pause(text="Press enter to continue..."):
  input(text)




def lobby(data, lobbyToken):
  pass



def joinLobby(data):
  print("1) Join With Code")
  print("2) Server List (Comming Soon)")

  cmd = input(": ")
  if cmd == "1":
    cls()
    
    code = input("Code: ")

    send_data = {
      "code":code,
      "token":data["token"]
    }

    ret = requests.post(link+"server/gamemanage", json=send_data)


    print(ret.text)

    pause()


def createLobby(data):
  cls()
  name = input("Lobby Name: ")
  public_text = input("Public (y or n): ")
  if public_text == "y" or public_text == "Y":
    public = 1
  else:
    public = 0

  data = {
    "token":data["token"],
    "process":"createLobby",
    "lobbyName":str(name),
    "type":public
  }

  ret = requests.post(link+"server/gamemanage", json=data)

  print(ret.text)

  #Goto lobby() after once joining is done

  pause()

def joinlobby(data):
  cls()
  print("")  



def main(data):
  header("Battles")
  print("1) Join Lobby")
  print("2) Create Lobby")
  print("3) Find Lobby")
  cmd = input(": ")

  if cmd == "1":
    pass
  elif cmd == "2":
    createLobby(data)
  elif cmd == "3":
    pass