
import re

s = []

x = open("data.txt")

for line in x:
    if line == "\n": break
    s.append([line[k * 4 + 1] for k in range(len(line) // 4)]) # this is just line[1::4] - thanks UnrelatedString

s.pop()
s = [list("".join(c).strip()[::-1]) for c in zip(*s)]

for line in x:
    a, b, c = map(int, re.findall("\\d+", line))
    s[c - 1].extend(s[b - 1][-a:])
    s[b - 1] = s[b - 1][:-a]

print("".join([a[-1] for a in s]))






