# Print the name(s) of any student(s) having the second lowest grade in.
# If there are multiple students, order their names alphabetically and print each one on a new line.

n = int(input())
records = []

for i in range(n):
    name = input()
    marks = float(input())

    records.append([name, marks])

marks = [i[1] for i in records]

dg = list(set(marks))
dg.sort()

final = [i[0] for i in records if i[1] == dg[1]]
final.sort()
for i in final:
    print(i)
    
