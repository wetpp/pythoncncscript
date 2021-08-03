import requests
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init()
loggedIn = "false"

def clear_screen():
  os.system("cls")


user = input("Enter your Username: ")
if user == "root":
  password = input("Enter your Password: ")
  if password == "sauce":
    print("Succesful login as " + user + ".")
    loggedIn = "true"

if user == "wetpp":
  password = input("Enter your Password: ")
  if password == "vNjT4NSaqq":
    print("Succesful login as " + user + ".")
    loggedIn = "true"



def cncLine():
  sleep(1.5)
  clear_screen()
  print(Fore.CYAN + "   _____ ______ _____  ______          _      ")
  print("  / ____|  ____|  __ \|  ____|   /\   | |     ")
  print(" | |    | |__  | |__) | |__     /  \  | |     ")
  print(" | |    |  __| |  _  /|  __|   / /\ \ | |     ")
  print(" | |____| |____| | \ \| |____ / ____ \| |____ ")
  print("  \_____|______|_|  \_\______/_/    \_\______|")
  print()
  
  Style.DIM
  cmd = input(Fore.CYAN + user + Fore.RESET + "@" + Fore.CYAN + "71.224.69.167:~# " + Fore.RESET + Style.RESET_ALL)
  
  
  if cmd == "help":
    print("Current commands: HELP, .tcp, .udp, .ovh, .ipinfo")
    cncLine()

  if cmd == ".ipinfo":
    ip = input("IP: ")
    r = requests.get("https://ipinfo.io/" + ip + "?token=c4c9305edc5432")
    data = r.json()
    if r.status_code == 404:
      print("Invalid IPINFO ip.")
      cncLine()
    
    city = data['city']
    state = data['region']
    country = data['country']
    postal = data['postal']
    isp = data['org']
    
    print("Location: " + city + ", " + state + ". " + country)
    print("Zip: " + postal)
    print("ISP: " + isp)
    sleep(3)
    cncLine()
  
  if cmd == ".tcp":
    print("This command is currently under development.")
  
  if cmd == ".udp":
    print("This command is currently under development.")
  
  if cmd == ".ovh":
    print("This command is currently under development.")
  
  while cmd not in ["help", ".tcp", ".udp", ".ovh", ".ipinfo"]:
    print("Invalid command")
    cncLine()

    

if loggedIn == "true":
  cncLine()
