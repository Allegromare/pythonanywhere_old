import inflect

p = inflect.engine()

words = p.number_to_words(1234)

print(words)
