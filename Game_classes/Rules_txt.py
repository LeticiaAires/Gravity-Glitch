
rel_path = "Assets/Rules.txt"
file = open (rel_path , "r")

for line in file.readlines():
    print(line)

file.close()
