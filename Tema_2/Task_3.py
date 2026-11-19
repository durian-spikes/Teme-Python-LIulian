import string

text = input("Text: ")

# Split the text into words
words = text.split()

# 1. Count words
word_count = len(words)

# 2. Count sentences
sentence_count = 0

for ch in text:
    if ch == "." or ch == "!" or ch == "?":
        sentence_count += 1

# 3. Count characters without spaces
characters = len(text.replace(" ", ""))

# 4. Count vowels
vowels = "aeiou"
vowel_count = 0

for ch in text.lower():
    if ch in vowels:
        vowel_count += 1

# Remove punctuation from the beginning and end of words
clean_words = []

for word in words:
    clean_word = word.strip(string.punctuation)

    if clean_word:
        clean_words.append(clean_word)

# 5. Find the longest word
if clean_words:
    longest_word = max(clean_words, key=len)
else:
    longest_word = ""

# 6. Find the three longest words
three_longest = sorted(clean_words, key=len, reverse=True)[:3]

# 7. Reverse the text
reversed_text = text[::-1]

# Print the report
print("Words:", word_count)
print("Sentences:", sentence_count)
print("Characters (no spaces):", characters)
print("Vowels:", vowel_count)
print("Longest word:", longest_word)
print("Three longest words:", ", ".join(three_longest))
print("Reversed:", reversed_text)