#Nathan Raia

sentence = input("Enter a sentence with no punctuation")
characters = len(sentence)
wordList = sentence.split(" ")
words = len(wordList)
average = 0
for i in wordList:
    chars = len(i)
    average = average + chars
average = average / words

print("There are" , characters , "characters in your sentence")
print("There are" , words , "words in your sentence")
print("The average word length is" , average)