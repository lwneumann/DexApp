import urllib.request  
from bs4 import BeautifulSoup 


def get_url(number):
    return f"https://www.serebii.net/pokedex-dp/{number:0>3}.shtml"


def get_text(url):
    # Open url 
    html = urllib.request.urlopen(url) 
    # Parse html
    htmlParse = BeautifulSoup(html, 'html.parser') 
    # Getting all paragraphs 
    text = ""
    for para in htmlParse.find_all("p"): 
        text += para.get_text()
    return text


def store_site(number, folder):
    # Get url
    url = get_url(number)
    # Get text
    text = get_text(url)
    # Write text
    with open(f"./{folder}/{number:0>3}.txt", 'w+', encoding="utf-8") as file:
        file.write(text)
    return
