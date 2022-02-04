with open("eng-words.txt", "r") as eng:
    li = eng.readlines()

li.sort()

with open("eng-words.txt", "w") as eng:
    for word in li:
        eng.write(word)
