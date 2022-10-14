def stip(array):
    for i in array:
        i.strip()
    return array


def search(array, item):
    for i in array:
        if i == item:
            print("found at index", array.index(i))


def main():
    array = list(map(int, map(stip, input("test").split(","))))
    search(array, 23)


main()
