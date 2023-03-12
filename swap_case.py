# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# i.e. 
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

s = 'Pythonist 2'

st = ''
for i in s:
    if i.isupper():
        st = st + i.lower()
    else:
        st = st + i.upper()

print(st)


