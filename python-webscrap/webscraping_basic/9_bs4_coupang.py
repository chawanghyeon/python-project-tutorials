from numbers import Rational
import re
import requests
import re
from bs4 import BeautifulStoneSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulStoneSoup(res.test, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs={"class":"rating"}).get_text()
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}).get_text()

    print(name, price, rate, rate_cnt)
