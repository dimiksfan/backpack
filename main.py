from readerCsv import getLst
from function import binMask, recSearch

def elemSum(lst):
    sumP = 0
    for i in range(len(lst)):
        sumP = sumP + int(lst[i]['price'])
    return sumP


def findAnsw(lst, maxW):

    answ = binMask(lst, maxW)
    print("Бин. маски:\n",answ,'\n',"Сумма:", elemSum(answ),'\n')
    answ = recSearch(lst, maxW)
    print("Рекурсия:\n",answ,'\n',"Сумма:", elemSum(answ),'\n')



lst = getLst('./numbers.csv')
maxW = 100
answ = []
findAnsw(lst, maxW)
