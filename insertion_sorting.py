def insert(vector, i):
    if len(vector) == 0:
        vector.append(i)
        return vector

    for idx, j in enumerate(vector):
        if i < j:
            vector.insert(idx, i)
            return vector

    vector.append(i)
    return vector

def insertion_sort(vector):
    sorted_vector = []

    for i in vector:
        sorted_vector = insert(sorted_vector, i)

    return sorted_vector


test_list_1 = [6, 7, 9, 8, 1, 2, 3, 4, 12]
test_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_list_3 = [5, 6, 7, 8, 9, 1, 2, 3, 4]

print('Tests')
print(insertion_sort(test_list_1))
print(insertion_sort(test_list_2))
print(insertion_sort(test_list_3))
