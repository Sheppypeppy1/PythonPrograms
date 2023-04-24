import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

content = requests.get(URL)
website_html = content.text

soup = BeautifulSoup(website_html, "html.parser")

movie_names_html = soup.find_all(name="h3", class_="title")
movie_names = [code.text for code in movie_names_html]
movie_names = movie_names[::-1]
print(movie_names)

with open("movies.txt", mode="w") as file:
    for movie in movie_names:
        file.write(f"{movie}\n")


