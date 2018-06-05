from collections import defaultdict
d = defaultdict(list)
# d[0].append(1)
# d[0].append(2)
# d[1].append(2)
# d[2].append(0)
# d[2].append(3)
# d[3].append(3)
d[0].append(1)
d[0].append(2)
dict = defaultdict(bool)


def dfs(curr):
    dict[curr] = True
    for i in d[curr]:
        if dict[i] == True:
            return True
        else:
            return dfs(i)
    if len(dict.keys()) == 4:
        return False

if(dfs(0)):
    print("Cycle")
else:
    print("No Cycle")
