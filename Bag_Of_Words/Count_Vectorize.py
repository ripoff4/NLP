# Same as Bag of Words but with CountVectorizer
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
sum = 0
for i in word_count:
    sum += word_count[i]
for i in word_count:
    word_count[i] = word_count[i]/sum
print("Word count:", word_count)
