"""
This is a very simple search engine just for beginners.

Heads Up: Copying without credit is restricted.

"""

text = input()
word = input()

def search(word):
    if word in text:
        return print("Word found")
    else:
        return print("Word not found")

search(word)
