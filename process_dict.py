filename = "twl3.txt"
file_ = open(filename)
for line in file_.readlines(): 
  line = line.strip()
  print(line)
