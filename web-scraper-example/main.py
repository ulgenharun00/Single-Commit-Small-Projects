import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.encoding = "UTF-8"

soup = BeautifulSoup(response.text, "html.parser")
rough_scraping = soup.find_all(name="h3", class_="title")

movie_list = []
for element in rough_scraping:
    movie_list.append(element.string.strip())

movie_list = [movie.replace("â\x80\x93", "–") for movie in movie_list]
movie_list.reverse()

with open("list.txt", "w", encoding="UTF-8") as file:
    for movie in movie_list:
        file.write(movie + "\n")