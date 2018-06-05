class data:
    def __init__(self,p,d):
        self.petrol = p
        self.dist = d

def find_starting_petrol_pump(array):
    start = 0
    end = 1
    current_petrol = array[start].petrol - array[start].dist
    while current_petrol < 0 or start != end:
        while current_petrol < 0 and start != end:
            current_petrol -= array[start].petrol - array[start].dist
            start = (start + 1)%len(array)
            if start == 0:
                return -1
        current_petrol += array[end].petrol - array[end].dist
        end = (end + 1) % len(array)
    return start


array = [data(4,6),data(6,5),data(7,3),data(4,5)]
print(find_starting_petrol_pump(array))