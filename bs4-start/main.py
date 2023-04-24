from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")

articles = [article.find(name="a") for article in soup.find_all(name="span",class_="titleline")]

article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.text
    article_texts.append(article_text)
    article_link = article_tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(upvote.text.split()[0]) for upvote in soup.find_all(name="span", class_="score")]

print("ARTICLE TEXTS -----------------------")
print(article_texts)
print("\n")
print("ARTICLE LINKS -----------------------")
print(article_links)
print("\n")
print("ARTICLE UPVOTES -----------------------")
print(article_upvotes)

highest_vote = max(article_upvotes)
index = article_upvotes.index(highest_vote)

print("\n")
print("INDEX AND HIGHEST SCORE -----------------------")
print(index, highest_vote)

print("\n")
print("POPULAR ARTICLE AND UPVOTES -----------------------")
print(article_texts[index], highest_vote)