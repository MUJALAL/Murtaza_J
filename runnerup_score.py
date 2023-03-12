# Given the participants score sheet for your University Sports Day, you are required to find the runner-up score. 
# You are given n scores.
# Store them in a list and find the score of the runner-up.

# n = 5
# [2 3 6 6 5]
# runner up = 5

n = int(input())
arr = map(int, input().split())

st = list(set(arr))
st.sort(reverse= True)
print(st[1])


