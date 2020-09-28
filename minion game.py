def minion_game(string):
    l = len(string)
    Stuart = Kevin = 0
    for i in range(l):
        if string[i] in "AEIOU":
            Kevin += l - i
        else:
            Stuart += l - i

    if Kevin > Stuart:
        print("Kevin", Kevin)
    elif Stuart > Kevin:
        print("Stuart", Stuart)
    else:
        print(draw)



if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
