""" 
    Simple script to scrape cat quotes from a website and store in a CSV file
    site_scraper.py 
    
    Andrew Tandy 2019
"""

from bs4 import BeautifulSoup
import requests

def scrape_site():
    """ Scrapes quotes from site """

    # Use requests and BS4 to scrape website into soup
    source = requests.get(f"https://cattime.com/cat-facts/lifestyle/1470-25-famous-quotes-about-cats").text
    soup = BeautifulSoup(source, "lxml")

    # After reviewing the above site, the information I wish to scrape is contained
    # within a simple ordered list.
    quote_content = soup.find("ol")

    # Prep an empty list ready to populate with quotes
    quotes = []

    for content in quote_content.find_all("li"):
        """ For loop iterating through list 'li' in ordered list 'ol' """

        # The below is mildly ugly due to not being able to split the string
        # at the symbol '-' using .split('-'). Not sure why, future investigation
        # needed.

        # Pull quote from content contained within <li> tag, convert to string and 
        # split at character '<'
        quote_split = str(content).split("<")

        # After content has been split, take the second item contained, which is [1]
        # This item still has HTML markup at the beginning of the string. We could split again
        # at '>', however it is simpler to just start from the 3rd character in using [3:]
        quote = quote_split[1][3:]

        # Pull author from content, conveniently located within an '<a>' tag, and strip the HTML
        # markup using .get_text()
        author = content.find("a").get_text()

        # Every time the loop runs through it will add quote and author to the quotes list prepared earlier
        quotes.append([quote,author])

    return quotes

