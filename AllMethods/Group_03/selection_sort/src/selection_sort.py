def selection_sort(list1):
    for i in range(len(list1)):
        min_index = i
        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        list1[i], list1[min_index] = list1[min_index], list1[i]

    return list1
