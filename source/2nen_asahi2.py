# coding: utf-8
import os
from flask import Flask
import requests
from bs4 import BeautifulSoup

#test
app = Flask(__name__)
@app.route('/')

def main():
	load_url = "https://www.asahi.com/articles/DA3S14459819.html?iref=pc_rensai_long_16_article"
	html = requests.get(load_url)

	soup = BeautifulSoup(html.content,"html.parser")

	topic1 = soup.find(class_ ="Title")
	topic2 = soup.find(class_ ="ArticleText")

	print(topic1.text)
	print(topic2.text)

    return "Hello world!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")
	
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000))) 