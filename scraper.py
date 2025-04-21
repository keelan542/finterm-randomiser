import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import string

# Define a base url
base_url = "https://www.investopedia.com/"

# Define path to terms
term_path_generic = "terms-beginning-with-"

# Define list of lowercase letters, with 'num' prepended
num_letters = list(string.ascii_lowercase)
num_letters.insert(0, 'num')

# Define integer that goes at end of each path
end_integer = 4769350

# Create empty list to hold full urls
full_term_paths = []

# Create full term paths
for num_letter in num_letters:
    full_term_paths.append(base_url + term_path_generic + num_letter + "-" + str(end_integer))
    end_integer += 1

# Creating instance of UserAgent
ua = UserAgent()

# Testing searching for a term
to_search = "ETF"
found_terms = []
for page in full_term_paths:
    # Make request for current page e.g. 'A' or 'B' terms
    headers = {'User-Agent': ua.random}
    page = requests.get(page, headers=headers)

    # Create soup
    soup = BeautifulSoup(page.content, "html.parser")

    # Get list of terms
    terms = soup.find_all("a", class_="dictionary-top300-list__list")

    # Attempt to find term
    for term in terms:
        if to_search.lower() in term.text.strip().lower():
            found_terms.append(term.text.strip())

# Printing results of search
if (len(found_terms) > 0):
    print("Found the following term(s):")
    for term in found_terms:
        print(term)
else:
    print(f"No results for '{to_search}'")