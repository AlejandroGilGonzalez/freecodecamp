import re

word = "haallal"

positions = re.finditer("a", word)

for match in positions:
    print(match.start())
    word = word[:match.start()] + "-" + word[match.start()+1:]

print(word)