def count_word_occurence(sentence):
    words=sentence.lower().split()
    word_count={}
    for word in words:
        word = word.strip(".,!\"'()[]{}")
        if word:
            word_count[word]= word_count.get(word,0)+1
    return word_count
sample_sentence="the quick brown fox jumps over the lazy dog! the fox was quick."
result=count_word_occurence(sample_sentence)
print("Word Occurence:")
for word , count in result.items():
    print(f"'{word}':{count}")