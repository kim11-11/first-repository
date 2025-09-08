def GetMinMax(data) :
    min_value = data[0]
    max_value = data[0]

    for val in data :
        if val < min_value :
            min_value = val;

    for i in range(1, eln(data)):
        if data[i] < min_value :
            min_value = data[i]
        if data[i] > max_value :
            max_value = data[i]
    return min_value, max_value

min_value, max_value = GetMinMax([5, 6, 3, 9, 8, 1, 4])
print(f"최솟값 : {min_value}")
print(f"최댓값 : {max_value}")
