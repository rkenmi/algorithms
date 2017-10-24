"""
Search for all sentences in a given string that match a given keyword and return them (in a list)
"""


def search_text_regex(text, keyword):
    import re

    #  use regex to sub-stitute parts of the string. Basically string.replace with regex
    text = re.sub(r'[\n]+', '', text)  # + = match 1 or more
    text = re.sub(r'[\s]{4,}', ' ', text)  # {4, } = match 4 or more

    #  use regex findall if you have more than 1 matches.
    sentences = re.findall(r'[\n\s]*([a-zA-Z\'\,0-9\-\s\n\"]*\.)', text)
    keyword = keyword.lower()
    return [s for s in sentences if keyword in s.lower()]


def search_text_non_regex(text, keyword):
    text = text.replace('.\n', ". ")
    text = text.replace("\n", " ")
    text = text.replace('                 ', " ")

    sentences = text.split(". ")
    keyword = keyword.lower()
    return [s+'.' for s in sentences if keyword in s.lower()]


