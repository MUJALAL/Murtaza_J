# STDIN           Function
# -----           --------
# abracadabra     s = 'abracadabra'
# 5 k             position = 5, character = 'k'


def stfunc(st, position, character):
    st = list(st)
    st[int(position)] = character
    print("".join(st))



if __name__ == '__main__':
    st = input()
    position, character = input().split()
    stfunc(st, position, character)


