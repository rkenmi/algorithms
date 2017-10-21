"""
Search for sentences in a given string that match a given keyword and return them (in a list)
"""

def search_text(text, keyword):
    import re

    sentences = re.findall(r'[\n]*([a-zA-Z\'\,0-9\-\s\n\"]*\.)', text)
    return [s for s in sentences if keyword.lower() in s.lower()]
