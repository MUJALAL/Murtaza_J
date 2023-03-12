# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# The first line contains the integer n, the number of students' records. 
# The next n lines contain the names and marks obtained by a student, each value separated by a space. 
# The final line contains query_name, the name of a student to query.



n = int(input())
dct = {}

for i in range(n):
    name, *line = input().split()
    dct[name] = line


query_name = input()


ln = 3
for i in dct:
    if i == query_name:
        dg = sum(map(float, dct[i])) / ln
        print("{:.2f}".format(dg))



# 2
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh