def stip(array):
    for i in array:
        i.strip()
    return array


def search_left(array, index, item):
    while index > 0 and array[index] == item:
        print("gasit si la pozitia", index + 1)
        index = index - 1


def search_right(array, index, item):
    while index < len(array) and array[index] == item:
        print("gasit si la pozitia", index + 1)
        index = index + 1


def binary_search(array, item):
    array.sort()
    low = 0
    high = len(array) - 1
    foundItem = 0
    foundIndex = -1

    while low <= high and foundItem == 0:
        mid = (high + low) // 2
        midItem = array[mid]
        if midItem == item:
            print("valoarea gasita la pozitia ", mid + 1)
            foundItem = 1
            foundIndex = mid
        else:
            if midItem > item:
                high = mid - 1
            else:
                low = mid + 1

    if foundItem == 0:
        print("nu s-a gasit elementul")

    search_left(arr, foundIndex - 1, item)
    search_right(arr, foundIndex + 1, item)


arr = list(map(int, map(stip, input().split(","))))
element = int(input())
binary_search(arr, element)
