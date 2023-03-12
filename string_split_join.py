# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

s = 'this is a string'

st = "-".join(s.split(" "))

print(st)