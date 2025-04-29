sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
print("Word count:", word_count)
