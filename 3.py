lst = [1,2,3,4,1,2, 2, 2]
sr = [a for a in set(lst) if lst.count(a) > 1]
print(sr)