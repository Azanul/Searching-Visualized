from OFA import *


def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        arr[mid].select()
        if arr[mid].h == x:
            return mid

        arr[mid].deselect()
        if arr[mid].h > x:
            return binary_search(arr, l, mid - 1, x)

        return binary_search(arr, mid + 1, r, x)

    return -1


def search():
    x = search_val.get()
    if blocks[0].h == x:
        return 0

    i = 1
    while i < 160 and blocks[i].h <= x:
        i *= 2

    blocks[binary_search(blocks, i // 2, min(i, 160 - 1), x)].found()
