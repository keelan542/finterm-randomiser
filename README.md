# Finterm Scraper

Short Python script that does the following:

1. Randomly chooses a letter
2. Requests page content of finterm dictionary for chosen letter (using [requests](https://pypi.org/project/requests/))
3. Scrapes a list of the financial terms on that page and their links (using [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/))
4. Randomly chooses a term
5. Opens url corresponding to that term in new tab of default browser
