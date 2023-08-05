import wikipedia

def scrape(name='facebook', length=2):
    """Simple program that scrapes a specified number of sentences from Wikipedia."""
    result = wikipedia.summary(name, sentences=length)
    return result
