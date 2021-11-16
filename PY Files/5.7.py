unique = []
with open("test.txt", "r") as file:
   lines = file.readlines()
   for line in lines:
       words = line.split()
       for word in words:
           word = word.strip()
           if word not in unique:
               unique.append(word)
unique = sorted(unique)
print(unique)
