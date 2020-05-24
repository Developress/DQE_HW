import re
from collections import Counter

n = int(input("Enter amount of letters:"))
content = open("C:\\DB\\words.txt").read()
words = re.findall(r'\b\w{' + str(n) + r'}\n', content)
letters = [i for word in words for i in word if i!='\n']

most_common = Counter(letters).most_common()
i = 0
pattern = ""

for i in range(0, n):
    pattern+="_"

while True:
    print("With probability", format((most_common[i][1]/len(letters))*100, '.2f'),
          "% your word", pattern,"contains '", most_common[i][0],
          "' letter. Am I right? Print y if yes or n if no")
    answer = input()
    if answer=="y":
        n-=1
        print("Please, enter the pattern of your word, including RIGHT positions "
              "of letters. Your previous pattern", pattern)
        pattern = input()
        words = re.findall(r'\b' + pattern.replace('_', '.') + r'\n', content)
        if(len(words) < len(most_common) - i):
            for j in range(0, len(words)):
                print("Is ", words[j], "your word? Print y if yes or n if no")
                answer = input()
                if answer == "y":
                    n = 0
                    break
                else:
                    i+=1
    if n == 0:
        break
    i+=1

print("Congratulations! Computer has guessed your word just with", i, "tries")