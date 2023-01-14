def binarySearchUP(array, x, low, high):
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] <= x:
            low = mid + 1
        elif array[mid] > x:
            high = mid - 1
    if low >= len(array):
        return 'X'
    else:
        return array[low]


def binarySearchDOWN(array, x, low, high):
    while low <= high:

        mid = low + (high - low) // 2

        if array[mid] < x:
            low = mid + 1
        elif array[mid] >= x:
            high = mid - 1
    if high < 0:
        return 'X'
    else:
        return array[high]


n_chimps = int(input())
chimps = list(map(int, input().strip().split()))[:n_chimps]
n_query = int(input())
query = list(map(int, input().strip().split()))[:n_query]

for q in query:
    first = binarySearchDOWN(chimps, q, 0, len(chimps) - 1)
    second = binarySearchUP(chimps, q, 0, len(chimps) - 1)

    print(first, " ", second)
