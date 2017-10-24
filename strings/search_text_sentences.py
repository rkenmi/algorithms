"""
Search for all sentences in a given string that match a given keyword and return them (in a list)
"""


def search_text_regex(text, keyword):
    import re

    #  use regex to sub-stitute parts of the string. Basically string.replace with regex
    text = re.sub(r'[\s]{4,}', ' ', text)  # {4, } = match 4 or more

    #  use re.findall if you have more than 1 matches, re.search otherwise
    #  here, chop off leading newlines/spaces, capture the rest
    sentences = re.findall(r'[\n\s]*([a-zA-Z\'\,0-9\-\s\n\"]*\.)', text)
    keyword = keyword.lower()
    return [s for s in sentences if keyword in s.lower()]


def search_text_non_regex(text, keyword):
    #  Have ". " constitute the end of a sentence
    if text[-1] == '.':
        text += " "

    text = text.replace('.\n', ". ")  # repair newlines after periods
    text = text.replace("\n", " ")  #  chop remaining newlines
    text = text.replace('                 ', " ")  # repair broken spaces

    sentences = text.split(". ")
    keyword = keyword.lower()
    return [s+'.' for s in sentences if keyword in s.lower()]


