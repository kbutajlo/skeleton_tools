import requests, json
from bs4 import BeautifulSoup


def amazon_price(soup: BeautifulSoup):
    return soup.findAll("span", attrs={"class": "aok-offscreen"})

def pushover_call():
    url = "https://api.pushover.net/1/messages.json"
    pushover_request = json.dumps([{"token": "xxx"},\
            {"user":"xxx"}, \
            {"message": "xxx"},
            {"title", "xxx"}])
    
    print(pushover_request)

if __name__ == "__main__":
    url = 'https://www.amazon.pl/dp/B0CHXLxxM376'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    all_span_tags = amazon_price(soup)
    if len(all_span_tags) > 0:
        print(all_span_tags[0].text.strip())
    else:
        print("no results")

    #pushover_call()