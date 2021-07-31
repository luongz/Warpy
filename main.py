import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
script_version = '1.0'
banner2 = """
\033[1;31;40m

 █     █░ ▄▄▄       ██▀███   ██▓███ ▓██   ██▓
▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓██░  ██▒▒██  ██▒
▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▓██░ ██▓▒ ▒██ ██░
░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒██▄█▓▒ ▒ ░ ▐██▓░
░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒▒██▒ ░  ░ ░ ██▒▓░
░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒▓▒░ ░  ░  ██▒▒▒ 
  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░░▒ ░     ▓██ ░▒░ 
  ░   ░    ░   ▒     ░░   ░ ░░       ▒ ▒ ░░  
    ░          ░  ░   ░              ░ ░     
                                     ░ ░     
                                     
                                   \033[1;37;40m  \n
"""

window_title = " WARP+ Data Sniper "
banner = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠖⠚⢉⣩⣭⡭⠛⠓⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠃⢀⡴⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀
⠀⠀⠀⠀⡾⠁⣠⠋⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀
⠀⠀⠀⣸⠁⢰⠃⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀
⠀⠀⠀⡇⠀⡾⡀⠀⠀⠀⠀⣀⣹⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀
⠀⠀⢸⠃⢀⣇⡈⠀⠀⠀⠀⠀⠀⢀⡑⢄⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⢸⠀⢻⡟⡻⢶⡆⠀⠀⠀⠀⡼⠟⡳⢿⣦⡑⢄⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⣸⠀⢸⠃⡇⢀⠇⠀⠀⠀⠀⠀⡼⠀⠀⠈⣿⡗⠂⠀⠀⠀⠀⠀⠀⠀⢸⠁
⠀⠀⡏⠀⣼⠀⢳⠊⠀⠀⠀⠀⠀⠀⠱⣀⣀⠔⣸⠁⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀
⠀⠀⡇⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀
⠀⢸⠃⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⢀⠀⠀⠀⠀⠀⣾⠀⠀
⠀⣸⠀⠀⠹⡄⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠸⠀⠀⠀⠀⠀⡇⠀⠀
⠀⡏⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⢀⣠⢶⡇⠀⠀⢰⡀⠀⠀⠀⠀⠀⡇⠀⠀
⢰⠇⡄⠀⠀⠀⡿⢣⣀⣀⣀⡤⠴⡞⠉⠀⢸⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣧⠀⠀
⣸⠀⡇⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢹⠀⠀⢸⠀⠀⢀⣿⠇⠀⠀⠀⠁⠀⢸⠀⠀
⣿⠀⡇⠀⠀⠀⠀⠀⢀⡤⠤⠶⠶⠾⠤⠄⢸⠀⡀⠸⣿⣀⠀⠀⠀⠀⠀⠈⣇⠀
⡇⠀⡇⠀⠀⡀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠸⡌⣵⡀⢳⡇⠀⠀⠀⠀⠀⠀⢹⡀
⡇⠀⠇⠀⠀⡇⡸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠮⢧⣀⣻⢂⠀⠀⠀⠀⠀⠀⢧
⣇⠀⢠⠀⠀⢳⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡎⣆⠀⠀⠀⠀⠀⠘
⢻⠀⠈⠰⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠘⢮⣧⡀⠀⠀⠀⠀
⠸⡆⠀⠀⠇⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠆⠀⠀⠀⠀⠀⠀⠀⠙⠳⣄⡀⢢⡀


                 
"""
os.system('title ' + window_title if os.name == 'nt' else 'PS1="\[\e]0;' +
          window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print (banner)
print (banner2)
print(
    ' Automatic Sniper WARP+ Data\n'
)

print("")
print(f"[-] Version: {script_version}")
print("--------")
print("[+] Writen In Python3")
print("[-] Code by Lê Quốc Thái - rewritten by luongz")
print("[-] FB : Trần Đình Lượng")
print("[+]Get Id = Settings>Advanced>Diagnostics>ID")
referrer = input("Enter Your WARP ID and Enter:")





def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)


def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))
	except Exception as error:
		print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run():
	try:
		install_id = genString(22)
		body = {
		    "key": "{}=".format(genString(43)),
		    "install_id": install_id,
		    "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
		    "referrer": referrer,
		    "warp_enabled": False,
		    "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
		    "type": "Android",
		    "locale": "en_EN"
		}
		data = json.dumps(body).encode('utf8')
		headers = {
		    'Content-Type': 'application/json; charset=UTF-8',
		    'Host': 'api.cloudflareclient.com',
		    'Connection': 'Keep-Alive',
		    'Accept-Encoding': 'gzip',
		    'User-Agent': 'okhttp/3.12.1'
		}
		req = urllib.request.Request(url, data, headers)
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return status_code
	except Exception as error:
		print("")
		print(error)


g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	sys.stdout.write("\r[+] Waiting...   [□□□□□□□□□□] 0%")
	os.system('cls' if os.name == 'nt' else 'clear')
	sys.stdout.flush()
	result = run()
	if result == 200:
		g += 1
		print(banner2)
		print(f"\n[🌸] ID: {referrer}")
		print(f"[😎] Successful +1GB Data")
		print(f"[🌸] Result: {g} \033[1;32;40m HITS \033[1;37;40m  | \033[1;37;40 {b} \033[1;31;40m BAD \033[1;37;40  \n")
		for i in range(60, 0, -1):
			sys.stdout.write(f"\r \033[1;37;40 [🚀] After  {i} seconds, script running again.")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print(banner2)
		print("[😔] Error .")
		print(f" {g} \033[1;32;40m HITS \033[1;37;40m  | \033[1;37;40 {b} \033[1;31;40m BAD \033[1;37;40")
		for i in range(10, 0, -1):
			sys.stdout.write(f"\r \033[1;37;40 [🚀] Retry after {i}s...")
			sys.stdout.flush()
			time.sleep(1)
