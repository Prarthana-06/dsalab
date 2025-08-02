text={"apple,bannana, orange,apple,orange"}
word_counts={}
for word in text:
    if word in word_counts:
        word_counts[word]+1
    else:
        word_counts[word]=1
    for word,count in word_counts.items():
        print(f"{word}:{count}")        