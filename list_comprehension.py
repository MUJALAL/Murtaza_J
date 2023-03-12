# Let's learn about list comprehensions! You are given three integers x,y and z representing the
# Print a list of all possible coordinates given by  on a 3D grid where the sum of i+j+k is not equal to n

# x = 1
# y = 1
# z = 1
# n = 2
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x = int(input())
y = int(input())
z = int(input())
n = int(input())


l = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(l)