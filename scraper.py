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

# test getting html for one path
ua = UserAgent()
# headers = {'User-Agent': ua.random}
# test = requests.get(full_term_paths[0], headers=headers)
# soup = BeautifulSoup(test.content, "html.parser")
# names = soup.find_all("a", class_="dictionary-top300-list__list")
# for name in names:
#     print(name.text)

# Testing searching for a term
to_search = "Derivative"
found = False
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
        if to_search in term.text.strip():
            found = True
        
    if found: break

print(found)