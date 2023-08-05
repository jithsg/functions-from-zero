#!/usr/bin/env python3
import wikipedia


def scrape(name="Facebook", length=2):
    result = wikipedia.summary(name, sentences=length)
    return result


print(scrape("wikipedia"))
