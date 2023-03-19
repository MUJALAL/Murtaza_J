string = 'ABCDCDC'

sub_string = 'CDC'
count = 0
ln = len(string)
m = 0


for i in range(ln):
    n = -1
    n = string.find(sub_string,m,ln)
    if n >= 0:
        count += 1
        m = n + 1
