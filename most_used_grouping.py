filename = "twl3.txt"
file_ = open(filename)
dictionary = {}
most_used_groupings = []
for line in file_.readlines():
  word = line.strip()
  grouping = ''.join(sorted(word))
  if grouping not in dictionary:
      dictionary[grouping] = 0
  dictionary[grouping] += 1
# print(dictionary)
maximum = max(dictionary, key=dictionary.get)
for grouping in dictionary:
    if dictionary[grouping] == dictionary[maximum]:
        most_used_groupings.append(grouping)
print(most_used_groupings, dictionary[maximum])
# print(maximum, dictionary[maximum])
