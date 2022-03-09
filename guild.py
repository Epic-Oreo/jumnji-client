from main import cls
import requests
import json
import random
global link
link = "https://jumnji-server.oredgaming.repl.co/"
def makeguild(data):
  id = random.randint(1, 1000000000000000000)
  token = data["token"]
  data = {
    "members":[{"id":token}],
    "guildid":id
    
  }

  res = requests.post(link + "server/makeguild", json=data)
  res_data = json.loads(res.text)
  print(res_data)
  input()
def start(data):
  cls()
  print("1) Make Guild")
  cmd = input(": ")
  cls()

  if cmd == "1":
    makeguild(data)

