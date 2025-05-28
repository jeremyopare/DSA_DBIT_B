list_words = ["Hello","world","python"]
word_count = {}
for word in list_words:
   if word in word_count:
      word_count[word] += 1
      # word_count[char] = word_count[char] + 1
      print(word_count)
   else:
        word_count[word] = 1
        print(word_count)

print(f"The final result is {word_count}")