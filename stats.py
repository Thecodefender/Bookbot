import re
def count_words(text):
    # words = text.split()
    words = re.findall(r'\w+', text)
    return len(words)