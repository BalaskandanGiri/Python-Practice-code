count = 0
def permutation(actual_string,container):
    global count
    if len(actual_string) == len(container):
        print(container)
        count += 1
        return
    for i in range(len(actual_string)):
        if actual_string[i] not in container:
            container += actual_string[i]
            permutation(actual_string,container)
            container = container[:-1]

permutation("abcdefghi","")
print(count)
'''
[7, 1, 3, 2, 4, 5, 6] ==> 0
[6, 1, 3, 2, 4, 5, 7] ==> 1
[5, 1, 3, 2, 4, 6, 7] ==> 2
[4, 1, 3, 2, 5, 6, 7] ==> 3
[2, 1, 3, 4, 5, 6, 7] ==> 4
[1, 2, 3, 4, 5, 6, 7] ==> 5

4 3 1 2 ==> 0
2 3 1 4 ==> 1
3 2 1 4 ==> 2
2 3 1 4 ==> 1
'''