filename = "twl3.txt"
file_ = open(filename)
dictionary = {}
for line in file_.readlines():
  word = line.strip()
  for letter in word:
      if letter not in dictionary:
          dictionary[letter] = 0
      dictionary[letter] += 1
print(dictionary)
