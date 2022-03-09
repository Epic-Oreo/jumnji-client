import os, json, random, time, requests
import game
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


def startup():
  pong = requests.post(link+"server/ping")
  if pong.status_code == 200:
    pass

  else:
    print("Server not responding correctly! ({})".format(pong.status_code))
    print("The server is probobly down or under maintenance.")
    if input("Press enter to quit...") == "bypass":
      pass
    else:
      quit()

  while True:
    header("startup")
    print("1) Login")
    print("2) Signup")
    print("9) Exit")
    
    inp = input(": ")
    if inp == "1":
      login()      
    elif inp == "2":
      signup()

    elif inp == "9":
      break
    
    else:

      header("Try Again")
      print("Not an option")
      pause()





def signup():
  header("Signup")
  username = input("Username: ")
  password = input("Password: ")
  
  #sets data
  data = {"user":username, "pw":password, "process":"signup"}

  res = requests.post(link + "server/usermanage", json=data)
  res_data = json.loads(res.text)
  if res_data["status"]:
    cls()
    print("Account created!")
    print("Now please Login")
    pause()
  else:
    header("Error")
    print(res_data["error"])
    pause()




def login():
  global link, user
  header("Login")
  user = input("Username: ")
  pw = input("Password: ")
  data = {"user":user,"pw":pw,"process":"login"}
  
  res = requests.post(link + "server/usermanage", json=data)
  res_data = json.loads(res.text)

  if res_data["status"]:
    token = res_data["data"]["token"]
    tmpinp = {"token":token, "user":user}
    game.home.main(tmpinp)
  else:
    header("Error")
    print(res_data["error"])
    pause()

if __name__ == "__main__":
  startup()