import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import string
import webbrowser
import random

# Define a base url
base_url = "https://www.investopedia.com/"

# Define path to terms
term_path_generic = "terms-beginning-with-"

# Define list of lowercase letters, with 'num' prepended
num_letters = list(string.ascii_lowercase)
num_letters.insert(0, 'num')

# Creating instance of UserAgent
ua = UserAgent()

# Pick random letter
num_letter_index = random.randint(0, 26)
num_letter = num_letters[num_letter_index]

# Define integer that goes at end of path
end_integer = 4769350 + num_letter_index

# Build path to page containing list of terms for random letter
num_letter_url = base_url + term_path_generic + str(end_integer)

# Make request for page
headers = {'User-Agent': ua.random}
page = requests.get(num_letter_url, headers=headers)

# Create soup
soup = BeautifulSoup(page.content, "html.parser")

# Get list of terms
terms = soup.find_all("a", class_="dictionary-top300-list__list")

# Randomly choose term
term_index = random.randint(0, len(terms))

# Open page of random term
term_url = terms[term_index]["href"]
webbrowser.open_new_tab(term_url)