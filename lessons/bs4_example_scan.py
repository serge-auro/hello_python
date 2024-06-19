from bs4 import BeautifulSoup
import requests


url = "https://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

text = soup.find_all("span", class_="text")
print(text)
author = soup.find_all("small", class_="author")
print(author)

# for j in range(len(text)):
#     print(f"article # {j + 1}")
#     print(text[j].text)
#     print(f"Author - {author[j].text}\n")

print("----------------------")
links = soup.find_all("a")

link_get_href = ""
link__href = ""

for link in links:
    link_get_href = link_get_href + link.get('href')
    link__href = link__href + link['href']

if link_get_href == link__href:
    print("Переменные равны")
else:
    print("Переменные не равны")