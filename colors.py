def color(color_, text):
  num1 = str(color_)
  num2 = str(text)
  return(f"\033[38;5;{num1}m{num2}\033[0;0m")

def bgcolor(fgcolor, bgcolor, text):
  return(f"\033[48;5;{bgcolor}m\033[38;5;{fgcolor}m{text}\033[0;0m")



def preset(colorName, text):

  # Rarity:
  # 1 = common
  # 2 = rare
  # 3 = Epic
  # 4 = Mythic

  # Elements:
  # 1 = Fire
  # 2 = Water
  # 3 = Air
  # 4 = Earth
  # 5 = Light
  # 6 = Darkness
  # 7 = Dream
  # 8 = Life
  tmp = None
  red = 196
  energy = 229
  money = 83
  

  common = 253 #dadada
  rare  = 33 #0087ff
  Epic = 201 #ff00ff
  Mythic = 220 	#ffd700
  Fire = 160 #d70000
  Water = 159 #afffff
  Air = 153 #afd7ff 
  Earth = 94 	#875f00
  Light = 229 #ffffaf
  Darkness = 239 	#4e4e4e
  Dream = 225 #ffd7ff
  Life = 46 #00ff00

  


  if colorName == "red":
    tmp = {'type':"fg","color":red}

  elif colorName == "Common":
    tmp = {"type":"fg", "color": common}
  elif colorName == "Rare":
    tmp =  {"type":"fg", "color": rare}
  elif colorName == "Epic":
    tmp = {"type":"fg", "color": Epic}
  elif colorName == "Mythic":
    tmp = {"type":"fg", "color": Mythic}
  elif colorName == "Fire":
    tmp = {"type":"fg", "color": Fire}
  elif colorName == "Water":
    tmp = {"type":"fg", "color": Water}
  elif colorName == "Air":
    tmp = {"type":"fg", "color": Air}
  elif colorName == "Earth":
    tmp = {"type":"fg", "color": Earth}
  elif colorName == "Light":
    tmp = {"type":"fg", "color": Light}
  elif colorName == "Darkness":
    tmp = {"type":"fg", "color": Darkness}
  elif colorName == "Dream":
    tmp = {"type":"fg", "color": Dream}
  elif colorName == "Life":
    tmp = {"type":"fg", "color": Life}
  elif colorName == "money":
    tmp = {"type":"fg", "color":money}
  elif colorName == "energy":
    tmp = {'type':"fg", "color":energy}

  if tmp:
    if tmp["type"] == "fg":
      return color(tmp["color"] , text)
    else:
      return bgcolor(tmp["color1"], tmp["color2"], text)
  else:
    return "INVALID COLOR!"

        
def color_test():
  pass

if __name__ == "__main__":
  import os
  os.system('cls' if os.name=='nt' else 'clear')

  print(' '.join([color(x, x) for x in range(256)]))

  print("tests: ")
  color_test()

  quit()
  #print("\nThe 256 colors scheme is:")
  