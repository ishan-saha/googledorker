import requests
from bs4 import BeautifulSoup as bs
import os

chars={"%23":"#","%24":"$","%26":"&","%2C":",","%2F":"/","%3A":":","%3B":";","%3D":"=","%3F":"?","%40":"@"}

url="https://www.google.com/search?q="


def main():

	filename=input('[*]Enter the file name:') #basic info for the file to put data in
	dork=input('\n[*]Enter the google dork:') # the dork that the program will use
	
	response=requests.get(url+dork+'&num=100') # the request being made to the google server
	
	soup=bs(response.content,"html.parser") #converting the response into parsable html

	
	data=soup.find_all("h3",{"class":"r"})
	links={}
	ar=""
	count=0
	for anchor in data:
		for link in anchor:
			links[link.text]=link.get("href")



	file= open(filename+".html",'w')
	file.write("<html><head><title>"+filename+"</title></head><body>")
	file.write("<h2> Dork results for "+dork+"</h2><br>")
	counter=1
	
	for text in links:
		ar=links[text]
		string=ar[ar.find("http"):ar.find("&")]
		for char in chars:
			string=string.replace(char,chars[char])

		try:
			file.write("<a href='"+string+"'><strong>"+str(counter)+":</strong>"+string+"</a><br>")
		except:
			pass
		#file.write("<a href='"+ar[start:end]+"'><strong>"+str(counter)+":</strong>"+text+"</a><br>")
		counter+=1
	file.write("</body></html>")
	file.close()
	print("\n[*] Operation successful! Please check the file!")
	print("\n[*] Exiting the script!")
	os.system("firefox "+filename+".html")



main()
