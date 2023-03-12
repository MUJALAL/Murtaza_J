# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

n = int(input())

l = []

for i in range(n):
    name, *line = input().split()
    inp = list(map(int,line))


    if name == 'insert':
        l.insert(inp[0], inp[1])
    elif name == 'remove':
        l.remove(inp[0])
    elif name == 'append':
        l.append(inp[0])
    elif name == 'sort':
        l.sort()
    elif name == 'pop':
        l.pop()
    elif name == 'reverse':
        l.reverse()
    else:
        print(l)