import os
import json
import random
import time 
import requests
import battles
global link
import guild
import shop
import utils

import colors

link = "https://jumnji-server.oredgaming.repl.co/"
def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def header(text, clsOn=True):
  if clsOn:
    cls()
  print("===|"+text+"|===")

def pause(text="Press enter to continue..."):
  input(text)


class home():

  def inventory(data):
    selector = 1
    cards = utils.getCards(data["token"])["data"]
    header("Inventory")
    for card in cards:
      tmpParse = utils.card_parse(card)
      print("{}) {}".format(selector, colors.preset(tmpParse["rarity"], card["name"])))
      selector += 1
    
    cmd = input(": ")
    work = False
    try:
      cmd = int(cmd) - 1
      work = True    
    except TypeError:
      pass
    except ValueError:
      pass

    if work:
      selected = (cards[cmd])
      parse_data = utils.card_parse(selected)
      header(selected["name"])
      if selected["abilitysInfo"]:
        # print(selected["abilitysInfo"])
        if selected["abilitysInfo"]["discription"] != "":
          print("Ability: {} ({})".format(selected["abilitysInfo"]["name"], selected["abilitysInfo"]["discription"]))
        else:
          print("Ability: {}".format(selected["abilitysInfo"]["name"]))
      print("Damage: {}".format(colors.preset("energy",selected["damage"])))
      print("Element: {}".format(colors.preset(parse_data["element"],parse_data["element"])))
      print("Health: {}".format(colors.preset("red",selected["health"])))
      print("Rarity: {}".format(colors.preset(parse_data["rarity"], parse_data["rarity"])))

      pause()


  def cardStuff(data):
    header("Card Menu")
    print("Money: {}".format(utils.money(data["data"]["money"])))
    print("1) Inventory")
    print("2) Pack Store")
    print("3) Trading Hall")
    print("4) Shop")
    cmd = input(": ")
    if cmd == "1":
      home.inventory(data)
    elif cmd == "2":
      shop.packShop(data)
    elif cmd == "3":
      shop.tradingHall.main(data)
    elif cmd == "4":
      shop.shop(data["token"])



  def main(data):
    while True:
      data = utils.update(data)
      header("Welcome {0}".format(data["user"]))
      print("Money: {}".format(utils.money(data["data"]["money"])))
      print("1) Cards (Buy, Sell, View)")
      print("2) Battle")
      print("3) Guilds")

      cmd = input(": ")
      if cmd == "1":
        home.cardStuff(data)
      elif cmd == '2':
        battles.main(data)
      elif cmd == "3":
        guild.start(data)

  




