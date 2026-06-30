import json

with open("file.txt","r") as file:
    text = file.read()

def count_words(text):
    words=text.split()
    words = [word.lower() for word in words]
    count={}
    for word in words:
        if word=="the" or word=="a" or word=="an" or word=="and" or word=="or" or word=="but" or word=="in" or word=="on" or word=="at" or word=="to" or word=="for" or word=="of" or word=="with" or word=="by" or word=="from" or word=="as" or word=="is" or word=="are" or word=="was" or word=="were" or word=="be" or word=="have" or word=="has" or word=="had" or word=="it" or word=="this" or word=="that" or word=="these" or word=="those" or word=="i" or word=="you": continue
        count[word] = count.get(word, 0) + 1
    return count

word_counts = count_words(text)
word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
print("Top 10 most common words:")
top_10_words = list(word_counts.items())[:10]
for word, count in top_10_words:
    print(f"{word}: {count}")

json_data = json.dumps(top_10_words, indent=4)
with open("word_counts.json", "w") as json_file:
    json_file.write(json_data)
