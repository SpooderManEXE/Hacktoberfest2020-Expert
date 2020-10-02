import requests
from bs4 import BeautifulSoup

def getUrl(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    result_search= soup.find('div')
    data=[]

    for result_item in result_search:
        item={}
        item['quote']=soup.find('span', 'text').text
        item['text']=soup.find('small', 'author').text
        data.append(item)
    return data

if __name__ == "__main__":
    import sys
    a = getUrl(str(sys.argv[1]))
    print(a)
    
# http://quotes.toscrape.com/