from collections import Counter
import re
import sys

file = open(sys.argv[1])
str = file.read()
list = re.split("[\s.,;]+", str)
i = 0
for item in list:
    list[i] = item.lower()
    i+=1
res = dict(Counter(list))
i = 1
for key in sorted(res.keys()):
    print(i, key, ":", res[key])
    i+=1
file.close()

