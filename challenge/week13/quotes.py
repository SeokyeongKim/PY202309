import re
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
from collections import Counter

# url address
url = "https://quotes.toscrape.com/tag/life/"
html = ur.urlopen(url)


# Read url address with html parser
soup = bs(html.read(), "html.parser")

# Create a list to store all words
all_words = []

# Extracting text from quotes
quotes = soup.find_all('div', {"class": "quote"})
for quote in quotes:
    # Extract a part of text from a quote
    quote_text = quote.find_all('span', {"class": "text"})
    for text in quote_text:
        # Extract words using regular expressions
        words = re.findall(r'\b\w+\b', text.text.lower())
        # Add extracted words to a list
        all_words.extend(words)

# Calculate word frequency
word_freq = Counter(all_words)

# Output the top 5 words that occurred the most
top_words = word_freq.most_common(5)
for word, count in top_words:
    print(f"{word}: {count}")