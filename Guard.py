# copyright (c) BL4CK DR460N
# codded by BL4CK DR460N
# team : Woll Cyber Team
# No Recoded No Recode
# coding=utf-8

# color
NL = "\033[0m" # normal
GL = NL+"\033[96;1m" # Blue aqua
BB = NL+"\033[34;1m" # Blue light
YY = NL+"\033[33;1m" # Yellow light
GG = NL+"\033[32;1m" # Green light
WW = NL+"\033[0;1m"  # White light
RR = NL+"\033[31;1m" # Red light
CC = NL+"\033[36;1m" # Cyan light
B = NL+"\033[34m"    # Blue
Y = NL+"\033[33;1m"    # Yellow
G = NL+"\033[32m"    # Green
W = NL+"\033[0;1m"     # White
R = NL+"\033[31m"    # Red
C = NL+"\033[36;1m"    # Cyan
# import all modules
import os,sys,time,hashlib,marshal,json
from getpass import *
try:
	import requests
except ImportError:
	print (R+"[-] module 'requests' not found")
	print (W+"[!]  'pip2 install requests'")
	sys.exit()

def logo():
	os.system("clear")
	""" Ini data penting
	    Dimohon jangan di ubah code nya"""
	exec marshal.loads('s\x98\x01\x00\x00banner = R+"""\n  |`-._/\\_.-`|\n  |    ||    |\n  |___o()o___|\n  |__((<>))__|\n  \\   o\\/o   / """+C+""" \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90"""+R+"""\n   \\   ||   /  """+C+""" \xe2\x95\xa0\xe2\x95\xa3\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\x91 \xe2\x95\xa6\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98 \xe2\x94\x82\xe2\x94\x82"""+R+"""\n    \\  ||  /   """+C+""" \xe2\x95\x9a    \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\xb4\xe2\x94\x98"""+R+"""\n     \'.||.\'    """+G+""" Codded By BL4CK DR460N"""+R+"""\n       ``"""\n')
	print banner

def login():
	""" Di sini saya mengambil token facebook
	    dengan metode login manual"""
	logo()
	print
	""" Disini kalian input username"""
	usr = raw_input(Y+"[?] Username : "+G)
	""" Disini Kalian Input Password,
	    getpass.getpass adalah module untuk menyembunyikan
	    text yg kalian input"""
	pas = getpass(Y+"[?] Password : "+G)
	""" Ini Adalah Data" Yg Di Butuhkan"""
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":usr,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pas,"return_ssl_resources":"0","v":"1.0"}
	sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+usr+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pas+'return_ssl_resources=0v=1.0'+API_SECRET
	""" Di Sini Password Akan Di Encrypt Menjadi Hash md5"""
	x = hashlib.new('md5')
        x.update(sig)
	data.update({'sig':x.hexdigest()})
	print Y+"[!] Getting Accsess Token "
	time.sleep(5)
	try:
		""" Disini Semua Data" Akan Di Cocokan"""
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		j = json.loads(r.text)
		""" Disini Token Akan Di Save"""
		sv = open("token.txt","w")
		sv.write(j['access_token'])
		sv.close()
		print G+"[+] Success Get Access Token"
		time.sleep(4)
		menu()
	except KeyError:
		print R+"[-] Failed Get Access Token"
		sys.exit()
	except requests.exceptions.ConnectionError:
		print R+"[-] No Connection"
		sys.exit()

def menu():
	""" Di Sini Saya Membaca Token Fb Nya"""
	try:
		tok = open("token.txt","r").read()
	except:
		login()
	logo()
	print W+"["+G+"1"+W+"].Turn On Guard"
	print W+"["+G+"2"+W+"].Turn Off Guard"
	print W+"["+G+"3"+W+"].Exit"
	pil(tok)

def pil(tok):
	""" Di Sini Kalian Input Menu Nya"""
	p = raw_input(Y+"[?] Choose : "+G)
	if not p:
		print R+"[-] Can Not Be empty"
		pil()
	elif p == '1' or p == '01':
		on = 'true'
		guard(tok,on)
	elif p == '2' or p == '02':
		off = 'false'
		guard(tok,off)
	else:
		pil()

def get_id(tok):
	r = requests.get("https://graph.facebook.com/me?access_token="+tok)
	id = json.loads(r.text)
	return id['id']

def guard(tok, enable=True):
	id = get_id(tok)
	""" ini adalah data"""
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % tok}
	r = requests.post('https://graph.facebook.com/graphql', data=data, headers=headers)
#	print r.text
	if '"is_shielded":true' in r.text:
		logo()
		print
		print G+"[+] Guard On"
		sys.exit()
	elif '"is_shielded":false' in r.text:
		logo()
		print
		print G+"[+] Guard Off"
		sys.exit()
	else:
		print R+"[-] Error"
		sys.exit()

if __name__ == '__main__':
	menu()
