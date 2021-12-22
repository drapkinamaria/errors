import re
import os

with open("words.txt", "w"):
    pass
with open("daughter.txt", "r") as file:
    f = file.read()

p = re.compile("([а-яА-Я-']+)")
res = p.findall(f)
lsWord = {}
for key in res:
    key = key.lower()
    if key in lsWord:
        value = lsWord[key]
        lsWord[key] = value + 1
    else:
        lsWord[key] = 1
sorted_keys = sorted(lsWord, key=lambda x: int(lsWord[x]), reverse=True)
for key in sorted_keys:
    s = str("{0}: {1}").format(key, lsWord[key])
    print(s)
with open("words.txt", "w") as f:
    for key in sorted_keys:
        f.write(key + "\n")
