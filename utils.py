import requests, json, colors
global link
link = "https://jumnji-server.oredgaming.repl.co/"


def getCards(token):
  data = {"token":token, "process":"getCards"}
  tmp = requests.post(link + "server/usermanage", json=data)
  return json.loads(tmp.text)

def money(ammount):
  return colors.preset("money", "${}".format(ammount))

def update(data):
  reqData = {"token":data["token"], "process":'update'}
  tmp = requests.post(link+"server/usermanage", json=reqData)
  return json.loads(tmp.text)


def card_parse(card):
  rarity = None
  element = None
  # print(card["rarity"], card["element"])
  

  if card["rarity"] == 1:
    rarity = "Common"
  elif card["rarity"] == 2:
    rarity = "Rare"
  elif card["rarity"] == 3:
    rarity = "Epic"
  elif card["rarity"] == 4:
    rarity = "Mythic"

  if card["element"] ==  1:
    element = "Fire" 
  elif card["element"] ==  2:
    element = "Water" 
  elif card["element"] ==  3:
    element = "Air" 
  elif card["element"] ==  4:
    element = "Earth" 
  elif card["element"] ==  5:
    element = "Light" 
  elif card["element"] ==  6:
    element = "Darkness" 
  elif card["element"] ==  7:
    element = "Dream" 
  elif card["element"] ==  8:
    element = "Life" 

  # print(rarity, element)
  # input("Press enter to continue...")
  return {
    "rarity":rarity,
    "element":element
  }

