# Without using any string methods, try to print the following:

# 123...n

# Example:
# n = 5 
# print the string 12345


n = int(input())

l = [str(i) for i in range(1,n+1)]

str = ''.join(l)

print(str)