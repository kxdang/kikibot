import requests
from bs4 import BeautifulSoup

def checkStock ():
    URL = 'https://shop.lululemon.com/p/men-pants/ABC-Pant-Slim-30/_/prod9700120?color=26865&sz=29'
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    OOS = soup.select("#purchase-attributes-size-notification-error")

    return bool(len(OOS) == 0)

