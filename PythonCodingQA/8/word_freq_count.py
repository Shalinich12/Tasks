def word_count(sentence):
    count = sentence.split()
    words = {}
    for word in count:

        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words
print(word_count("python is easy and python is fun"))
