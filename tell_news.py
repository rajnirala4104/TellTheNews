#library for our project
from dotenv import load_dotenv
import requests as rq
import json
import translate
import os

# This script fetches the top news headlines from the NewsAPI and saves them in a text file

# Load the API key from the .env file
load_dotenv()

# Construct the URL for the NewsAPI request
url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={os.getenv('API_KEY')}"

# Send a GET request to the NewsAPI and retrieve the response as text
response = rq.get(url).text

# Parse the JSON response into a Python dictionary
news_data = json.loads(response)

# Extract the articles from the news data
articles = news_data["articles"]

# Create a file to store the news headlines
with open('news.txt', 'w', encoding='utf-8') as file:
    # Write each article's title to the file
    for article in articles:
        file.write(f"{article['title']}, let's know the next news.\n")

# Read the contents of the file
with open('news.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Use the translate module to speak the contents of the file in Hindi
translate.speak(text, "hi")
