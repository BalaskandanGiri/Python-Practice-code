data = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

def func(i,j,data):
    if i < 0 or j < 0 or i >= len(data) or j >= len(data):
        return
    if data[i][j] != 1:
        return
    data[i][j] = 2
    func(i+1,j,data)
    func(i,j+1,data)
    func(i - 1, j, data)
    func(i, j - 1, data)
    func(i + 1, j + 1, data)
    func(i + 1, j - 1, data)
    func(i - 1, j + 1, data)
    func(i - 1, j - 1, data)
count = 0
for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j] == 1:
            count += 1
            func(i,j,data)
print(count)