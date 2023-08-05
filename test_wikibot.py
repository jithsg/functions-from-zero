from wikibot import scrape

# Write a test function for scrape using assert


def test_scrape():
    assert "Microsoft" in scrape("Microsoft")
    assert "facebook" in scrape("facebook")
