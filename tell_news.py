import requests as rq
import json
import translate
import os
url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=f69e2dbdc9af4bddaf2a992b101235e1"
news = rq.get(url).text
News = json.loads(news)
Articles = News["articles"]
for heading in Articles:
    title = heading['title']
    content = heading['content']
    description = heading['description']
    f = open('news.txt', 'a', encoding='utf-8')
    f.write(f"{title}, let's know the next news.\n")
    f.close()

ft = open('news.txt', 'r', encoding='utf-8')
Text = ft.read()
translate.speak(Text, "hi")
ft.close()
# with open('news.txt', 'r', encoding='utf-8') as ft:
#     Text = ft.read()
#     translate.speak(Text, "hi")
os.remove('news.txt')

# translate.speak("My name is raj nirala, have you heard my name?", "hi")