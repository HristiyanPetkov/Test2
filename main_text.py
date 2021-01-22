from search_text import search_and_replace_text

text = "This is a text longer than two sentences and this is the first one. This is the second sentence."
print(text)
phrase = input("What phrase do you want to search for.")

print(search_and_replace_text(phrase, text))
