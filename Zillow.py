import requests
from bs4 import BeautifulSoup
# import lxml

ZILLOW_LINK = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22m" \
              "apBounds%22%3A%7B%22north%22%3A37.871971656195164%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A" \
              "37.678485658229235%2C%22west%22%3A-122.63417331103516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3A" \
              "true%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%" \
              "7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22v" \
              "alue%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22" \
              "fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22val" \
              "ue%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A203" \
              "30%2C%22regionType%22%3A6%7D%5D%7D"


class ZillowScraper:

    def __init__(self):
        # self.location = input("What address/location? ")
        # self.distance = input("Within what range in Kilometers? ")
        # self.price_min = int(input("Minimum price per month (£)? "))
        # self.price_max = int(input("Maximum price per month (£)? "))
        # self.rooms = int(input("Minimum number of bedrooms? (5 maximum) "))
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/106.0.0.0 Safari/537.36",
            "Accept-Language": "en-US"
        }
        self.address_list = []
        self.price_list = []
        self.link_list = []
        self.scrape_info()

    def scrape_info(self):
        response = requests.get(
            url=ZILLOW_LINK,
            headers=self.headers
        )
        web = response.text
        soup = BeautifulSoup(web, "html.parser")
        property_list = soup.find_all(
            name="li",
            class_="ListItem-c11n-8-73-8__sc-10e22w8-0 srp__hpnp3q-0 enEXBq with_constellation"
        )
        for location in property_list:
            if location.text != "":
                self.address_list.append(location.find_next(name="address").text)
                self.price_list.append(location.find_next(name="span").text.split()[0].strip("+/mo"))
                # if "https://www.zillow.com" in location.find_next(name="a")["href"]:
                #     self.link_list.append(location.find_next(name="a")["href"].strip("https://www.zillow.com"))
                # else:
                self.link_list.append(location.find_next(name="a")["href"])
        print(self.link_list)
