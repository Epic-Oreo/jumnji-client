import os, json, random, time, requests
import utils
from utils import card_parse
global link

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

def shop(token):
  header("Shop")
  data = {
    "process":"getShopItems",
    "token":token
  }
  ret = requests.post(link+"server/shopmanage", json=data)

  retData = json.loads(ret.text)

  if retData["status"]:
    selector = 1
    data = retData["data"]["cards"]
    print("Money: {}".format(colors.preset("money", "${}".format(retData["data"]["userMoney"]))))
    for x in data:
      tmpCardParse = card_parse(x["cardData"])
      print("{}) {} ({})".format(selector, colors.preset(tmpCardParse["rarity"],x["cardData"]["name"]), colors.preset("money","${}".format(x["price"]))))
      selector += 1
    cmd = input(": ")
    work = False
    try:
      cmd = int(cmd)
      work = True
    except TypeError:
      print("That needs to be a int")
      pause()
    except ValueError:
      pass
    if work:
      limit = len(data) - 1
      cmd = cmd - 1
      if cmd <= limit:
        cls()
        selected = data[cmd]
        parse_data = card_parse(selected["cardData"])
        abilityDisc = "No Ability"
        if selected["cardData"]["ability"]:
          tmpDisc = ""
          if selected["abilityDisc"]["discription"] != "":
            tmpDisc = selected["abilityDisc"]["discription"]
          else:
            tmpDisc = "No Discription"

          abilityDisc = "{} ({})".format(selected["abilityDisc"]["name"], tmpDisc)

        header((selected["cardData"]["name"]))
        print()
        print("Ability: {}".format(abilityDisc)) 
        print("Damage: {}".format(selected["cardData"]["damage"])) 
        print("Element: {}".format(colors.preset(parse_data["element"],parse_data["element"])))
        print("Health: {}".format(selected["cardData"]["health"]))
        print("Rarity: {}".format(colors.preset(parse_data["rarity"], parse_data["rarity"])))
        print("Price: ${}".format(selected["price"]))

        tmpCmd = input("Please conferm (y or n): ")
        if tmpCmd == "y" or tmpCmd == "Y" or tmpCmd == "yes" or tmpCmd == "Yes":

          sendData = {
            "token": token,
            "item": selected["id"],
            "process": "buyItem"
          }

          res = requests.post(link+"server/shopmanage", json=sendData)
          resData = (json.loads(res.text))
          if resData["status"]:
            print(resData["data"])
          else:
            cls()
            print("Error: {}".format(resData["error"]))
          pause()


          pass # Buy action
        else:
          pass
      else:
        print("That not a item")
        pause()

  else:
    print("Error {0}".format(retData["error"]))
    quit()

  #pause()





class tradingHall():
  def browse(data):
    userToken = data["token"]
    initReqData = {
      "token":data["token"],
      "process":"getPlayerShop"
    }
    ret = requests.post(link+"server/shopmanage", json=initReqData)
    ret = json.loads(ret.text)
    if ret["status"]:
      data = ret["data"]["cards"]
      money= ret["data"]["money"]
      selector = 1
      header("Trade Hall")
      print("Money: {}".format(colors.preset("money","${}".format(money))))
      print("*You can only see others items")
      for item in data:
        tmpCardParse = card_parse(item["cardInfo"])
        print("{}) {} (Price: {}  Seller: {})".format(selector, colors.preset(tmpCardParse["rarity"],item["cardInfo"]["name"]), colors.preset("money","${}".format(item["price"])), item["creator"]["name"]))
        selector += 1
      cmd = input(": ")

      if cmd == "":
        pass
      else:
        work = False
        try:
          cmd = int(cmd) - 1
          work = True

        except TypeError:
          print("That needs to be a number!")
          pause()
        except ValueError:
          pass

        if work:
          selected = (data[cmd])
          parse_data = card_parse(selected["cardInfo"])
          abilityDisc = selected["abilityDisc"]

          header((selected["cardInfo"]["name"]))
          print()
          print("Seller: {}".format(selected["creator"]["name"]))
          print("Ability: {}".format(abilityDisc)) 
          print("Damage: {}".format(colors.preset("energy",selected["cardInfo"]["damage"])))
          print("Element: {}".format(colors.preset(parse_data["element"],parse_data["element"])))
          print("Health: {}".format(colors.preset("red",selected["cardInfo"]["health"])))
          print("Rarity: {}".format(colors.preset(parse_data["rarity"], parse_data["rarity"])))
          print("Price: {}".format(colors.preset("money","${}".format(selected["price"]))))

          confirm = input("please enter 'yes' to confirm: ")
          if confirm == "yes":
            data = {
              "process":"buyPlayerItem",
              "token":userToken,
              "item":selected["id"]
            }
            ret = requests.post(link+"server/shopmanage", json=data)

            ret = json.loads(ret.text)

            if ret["status"]:
              print(ret["data"])
            else:
              print(ret["error"])
            pause()



    else:
      print("an error occurred! ({})".format(ret["error"]))

      pause()

  def sell(data):
    header("Sell Card")
    cards = utils.getCards(data["token"])
    cards = (cards["data"])
    selector = 1
    ids = []
  
    for card in cards:
      ids.append(card["id"])
      print("{}) {}".format(selector, card["name"]))
      selector += 1

    cmd = input(": ")
    work = False
    try:
      cmd = int(cmd) - 1
      work = True
    except TypeError or ValueError:
      print("You cant do that :(")
      pause()
    if work:
      price = input("price: ")
      header("Confirmation")
      print("are you sure you want to sell {} for ${}".format(cards[cmd]["name"], price))
      work = False
      try:
        price = int(price)
        work = True

      except TypeError or ValueError:
        print("Sumthin wrong")
        pause()


      if work:
        if input("please enter \"yes\": ") == "yes":
          sellData = {
            "token":data["token"],
            "cardID":ids[cmd],
            "price":price,
            "process":"postItem"
          }
          ret = requests.post(link+"server/shopmanage", json=sellData)

          retData = json.loads(ret.text)
          if retData["status"]:
            print(retData["data"])
          else:
            print("Error: {}".format(retData["error"]))
          pause()

  def main(data):
    header("Trading Hall")
    print("1) Browse Hall")
    print("2) Sell Card")
    cmd = input(": ")
    if cmd == "1":
      tradingHall.browse(data)

    elif cmd == "2":
      tradingHall.sell(data)



def packShop(data):
  #getPacks
  header("Pack Shop")
  print("Money: {}".format(utils.money(data["data"]["money"])))
  initReqData = {"process":"getPacks"}
  packsReq = requests.post(link+"server/shopmanage", json=initReqData)
  packs = json.loads(packsReq.text)["data"]
  selector = 1
  for pack in packs:
    print("{}) {} ({})".format(selector, pack["name"], colors.preset("money", "$"+str(pack["price"]))))

    selector += 1

  cmd = input(": ")
  work = False
  try:
    cmd = int(cmd) - 1
    selected = packs[cmd]
    work = True
  except IndexError:
    print("Thats not a option!")
    pause()
  except ValueError:
    print("Input Error!")
    pause()
  except TypeError:
    print("Hey that needs to be a number!")
    pause()

  if work:
    header("{} Pack".format(selected["name"]))
    print("Price: {}".format(utils.money(selected["price"])))
    print("Items:")
    for item in selected["items"]:
      if item["type"] == "money":
        print("• {}".format(utils.money(item["ammount"])))
      else:
        name = item["cardDetails"]["name"]
        parse = utils.card_parse(item["cardDetails"])
        print("• {}".format(colors.preset(parse["rarity"], name)))
    
    print("Are you sure you want to purchase this pack?")
    if input("(y or n): ") == "y":
      purchaseData = {
        "process":"buyPack",
        "token":data["token"],
        "packId":selected["id"]
      }
      buyRet = requests.post(link+"server/shopmanage", json=purchaseData)
      buyRet = json.loads(buyRet.text)

      if buyRet["status"]:
        draw = buyRet["data"]
        cls()
        for x in range(2):
          print("Opening")
          time.sleep(0.4)
          cls()
          print("Opening.")
          time.sleep(0.4)
          cls()
          print("Opening..")
          time.sleep(0.4)
          cls()
          print("Opening...")
          time.sleep(0.4)
          cls()
        #print(draw)
        if draw["type"] == "card":
          cardParse = utils.card_parse(draw["cardData"])
          print("You Drew: {}".format(colors.preset(cardParse["rarity"], draw["cardData"]["name"])))
        else:
          print("You Drew: {}".format(utils.money(draw["ammount"])))
        pause()
      else:
        print(buyRet["error"])
        pause()