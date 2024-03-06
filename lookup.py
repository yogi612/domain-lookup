#!/usr/bin/python
# Author : Yogendra Singh


import re
import os
import requests
from bs4 import BeautifulSoup as parser

ses = requests.Session()

class Domain:
	def __init__(self, url):
		os.system("clear")
		domain = input(" [?] Please Insert Domain : ")
		while domain in (""):
			domain = input(" [?] Insert Domain : ")
		self.url = (f"{url}/{domain}")

	def lookup(self):
		try:
			a = ses.get(self.url, headers={"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}).text
			b = parser(a, "html.parser")
			for x in b.find_all("pre"):
				try:
					domain_id = re.findall(r"\bD\w+\s\bI\w+.*", str(x))[0]
				except UnboundLocalError:
					domain_id = ("Domain ID: Tidak Terdeteksi")
				domain_name = re.findall(r"\bD\w+\s\bN\w+.*", str(x))[0]
				created = re.findall(r"\bC\w+\s\w+.*", str(x))[0]
				last_update = re.findall(r"\bL\w+\s\w+\s\w+.*\S", str(x))[0]
				expired = re.findall(r"\bE\w+\s\w+.*", str(x))[0]
				ns1 = re.findall(r"\bN\w+\s\w+.*", str(x))[1]
				ns2 = re.findall(r"\bN\w+\s\w+.*", str(x))[2]
		except UnboundLocalError:
			exit("\n [!] IP  Request")
		lib = [
			domain_id, 
			domain_name, 
			created, 
			last_update, 
			expired, 
			ns1, 
			ns2
		]
		self.tampil(lib)

	def tampil(self, lib):
		print("\n [ DOMAIN LOOKUP FROM WHOIS.COM ]\n")
		for i in lib:
			print(f" [*] {i}")
		exit("\n [!] Exit: Site Data Domain")

run = Domain("https://www.whois.com/whois/")
run.lookup()
