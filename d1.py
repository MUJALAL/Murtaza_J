# adding a comment to identify change to make
def is_leap(year):

    leap = False
    
    if year % 4 == 0:

        if year % 100 == 0 and year % 400 == 0:
                print('3print', year % 400)
                leap = True
        elif year % 100 != 0:
            leap = True
    else:
            leap = False
    
    
    return leap

year = int(input())
print(is_leap(year))
