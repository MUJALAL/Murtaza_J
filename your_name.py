# The first line contains the first name, and the second line contains the last name.

# Hello Ross Taylor! You just delved into python.


def print_full_name(first, last):
    # Write your code here
    print("Hello {0} {1}! You just delved into python.".format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)