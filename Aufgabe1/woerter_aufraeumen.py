import codecs
import re

list1 = codecs.open(" hier den absoluten file path eingeben ", "r", "UTF-8").readlines()

blank = list1[0].split()
words = list1[1].split()

for i in range(len(blank)):
    blank[i] = re.sub(r'\W+', '', blank[i])

print(blank)
print(words)

def possible_match():
    for i in blank:
        for j in words:
            if len(i) == len(j):
                same_length = [i, j]
                if same_character(same_length[0]):
                    print(same_length)
                for k in range(len(same_length[0])):
                    if same_length[0][k] == same_length[1][k]:
                        print(same_length)
                
def same_character(s):
    for i in range(1, len(s)):
        if s[i] != s[0]:
            return False
    return True

possible_match()



