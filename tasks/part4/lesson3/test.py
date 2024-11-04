def bubble_sort(arr: list) -> list:
    count = 0
    flag = True
    right = len(arr)
    while flag:
        flag = False
        for i in range(right - 1):
            count += 1
            if arr[i] > arr[i + 1]:
                flag = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
    return count


def bubble_sort1(arr: list) -> list:
    count = 0
    for i in range(len(arr)):
        for j in range(i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return count

a = range(1000)

b = sorted(a)

#count = bubble_sort(b)
count2 = bubble_sort1(b)

print(count2)
