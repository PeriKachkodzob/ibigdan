import requests
from time import sleep
from bs4 import BeautifulSoup

url = 'https://api.telegram.org/bot'
token = '451250718:AAH0S2cFVjfoCgatRG06PiBO9tlsPeeh2Bc'
chat_id = 385220023

headers = []

html = requests.get('http://ibigdan.com')
soup = BeautifulSoup(html.text, 'html.parser')
tags = soup.findAll('h2')

for tag in tags:
    headers.append(tag.get_text())

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + token + '/sendMessage', data=params)
    return response
    
def main():
    while True:
        html = requests.get('http://ibigdan.com')
        soup = BeautifulSoup(html.text, 'html.parser')
        tags = soup.findAll('h2')
        for tag in tags:
            header = tag.get_text()
            if header not in headers:
                send_mess(chat_id, header)
                headers.append(header)
        sleep(300)

main()
