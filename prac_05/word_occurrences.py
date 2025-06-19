"""
Word Occurrences
Estimate: 30 minutes
Actual:   22 minutes
"""
text = input("Enter text: ")
words = text.split()
word_dict = {}
for word in words:
    word = word.lower()
    word_dict[word] = word_dict.get(word,0) + 1
