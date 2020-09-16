from math import sqrt

def solution(area):
    tmp = area
    res = []
    while area > 0:
        sq = sqrt(tmp)
        if sq == int(sq):
            res.append(tmp)
            area -= tmp
            tmp = area
            continue
        tmp -= 1
    return res
