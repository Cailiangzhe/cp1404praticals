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
max_len = max(len(word) for word in word_dict)
for word in sorted(word_dict):
    print(f"{word:{max_len}}:{word_dict[word]}")