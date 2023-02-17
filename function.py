def binMask(lst, maxW=100):
    combs = []
    n = len(lst)
    for i in range(1 << n):  # combo = 9 -> 1001
        combo = []
        for pos in range(n):
            mask = 1 << pos
            if bool(i & mask):
                combo += [lst[pos]]
                s += int(lst[pos]['weight'])
        if s <= maxW: combs =+ [combo]
        
        
    return findMax(combs)


def findMax(lst):
    maxP = 0
    answ =[]
    for item in lst:
        curP = 0 
        for pos in range(len[item]):
            curP =+ int(item[pos]['price'])
            if curP > maxP:
                maxP = curP
                answ = item
    return answ
