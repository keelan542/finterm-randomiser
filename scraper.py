import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import string
import webbrowser

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

# Searching for term
to_search = "stock"
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
            link = term["href"]
            name = term.text.strip()
            found_terms.append((link, name))

# Printing results of search
if (len(found_terms) > 0):
    print("Found the following term(s):")
    for i, term in enumerate(found_terms):
        print(f"{i}. {term[1]}")
else:
    print(f"No results for '{to_search}'")
    exit()

# Ask user to choose from results
choice = input("Choose term: ")
chosen_term = found_terms[int(choice)]
print("You chose", chosen_term[1])

# Make request to page of chosen term
chosen_term_url = chosen_term[0]
webbrowser.open_new_tab(chosen_term_url)