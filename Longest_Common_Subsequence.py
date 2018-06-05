import time

dict = dict()

def LCS(str1, str2, l1, l2):
    string = str(str1) + str(str2) + str(l1) + str(l2)
    if(string in dict):
        return dict[string]
    if l1 < 0 or l2 < 0:
        return 0
    if str1[l1] == str2[l2]:
        dict[string] = 1 + LCS(str1, str2, l1 - 1, l2 - 1)
        return dict[string]
    else:
        dict[string] = max(LCS(str1, str2, l1 - 1, l2), LCS(str1, str2, l1, l2 - 1))
        return dict[string]


t1 = time.time()
str1 = "ABCDGHRAKSDL"
str2 = "AEDFHRASHDGA"
print(LCS(str1, str2, len(str1) - 1, len(str2) - 1))
print(time.time() - t1)
