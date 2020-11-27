
def merge(sub_arr, p, q):
    left = []
    right = []

    for i in range(p):
        left.append(sub_arr[i])

    for i in range(q-p):
        right.append(sub_arr[p+i])

    left.append('n')
    right.append('n')

    j = k = 0
    for i in range(q):
        if left[j] < right[k]:
            sub_arr[i] = left[j]
            j += 1
        else:
            sub_arr[i] = right[k]
            k += 1


def merge_sort(arr):
    if len(arr) > 1:
        leftSide = arr[:len(arr)/2]
        rightSide = arr[len(arr)/2:]
        leftSide = merge_sort(leftSide)
        rightSide = merge_sort(rightSide)
        arr = leftSide + rightSide
        merge(arr, len(arr)/2, len(arr))

    return arr


def main():
    f = open('info.txt', 'r')
    lista = f.read().split(",")
    f.close()
    merge_sort(lista)
    print(len(lista))


main()
