# url = 'https://www.simplytech.dev'


import requests
from bs4 import BeautifulSoup
from spellchecker import SpellChecker
import re

# URL of the webpage to scrape
url = 'https://www.simplytech.dev'

# Initialize the spell checker
spell = SpellChecker()

# Retrieve the webpage HTML and parse it with Beautiful Soup
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the text from the webpage and preprocess it
text = soup.get_text()
text = text.replace('\n', ' ')

# Use regular expressions to split text into words and punctuation
words_and_punctuation = re.findall(r"\b\w[\w']*([^\w']\w[\w']*)*\b|[^\w\s]", text)

# Check each word for spelling errors
misspelled = []
for token in words_and_punctuation:
    # Ignore punctuation tokens
    if re.match(r"[^\w\s]", token):
        continue
    # Check spelling of word tokens
    corrected = spell.correction(token)
    if corrected != token:
        misspelled.append(token)

# Print out any misspelled words
for word in misspelled:
    print(f"{word} is misspelled.")
