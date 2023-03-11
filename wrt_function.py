# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

# 2000 and 1800

def leap(num):



    if num % 4 == 0 and num % 100 == 0 and num % 400 == 0:
            return True
    elif num % 4 == 0 and num % 100 == 0 and num % 400 != 0:
            return False
    elif num & 4 == 0:
          return True
    else:
        return False

num = int(input())

res = leap(num)
print(res)