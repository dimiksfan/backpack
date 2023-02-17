def binMask(lst, maxW=100):
    combs = []
    n = len(lst)
    for i in range(1 << n):  # combo = 9 -> 1001
        s = 0
        combo = []
        for pos in range(n):
            mask = 1 << pos
            if bool(i & mask):
                combo += [lst[pos]]
                s += int(lst[pos]['w'])
        if s <= maxW: combs =+ [combo]              
    return findMax(combs)


def recSearch(lst, maxW=100):
    def rec(combo, deep):
        if deep == len(lst):  # точка останова
            if (noWay(combo, maxW)):
                combs.append(combo)
        else:  # шаги рекурсии
            rec(combo+[lst[deep]], deep+1)
            rec(combo, deep+1)
            combs = []
            rec([], 0)
            return findMax(combs)


def findMax(lst):
    maxP = 0
    answ =[]
    for item in lst:
        curP = 0 
        for pos in range(len[item]):
            curP =+ int(item[pos]['p'])
            if curP > maxP:
                maxP = curP
                answ = item
    return answ


def noWay(lst, maxW=100):
    sumW = 0
    for i in range (len(lst)):
        sumW = sumW + int(lst[i]['w'])
        if sumW <= maxW:
            return True
        return False
