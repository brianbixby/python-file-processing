filename = "twl3.txt"
file_ = open(filename)
longest_words = []
longest_word = ""
for line in file_.readlines():
  word = line.strip()
  if len(word) > len(longest_word):
      longest_word = word
      longest_words = []
      longest_words.append(word)
  elif len(word) == len(longest_word):
      longest_words.append(word)
if len(longest_words) > 1:
    print(longest_words)
    print(len(longest_words))
else:
    print(longest_word)
