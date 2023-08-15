def sum_for(arr):
    total = 0
    for x in arr:
        total += x
    return total


def sum_recursion(list):
    if not len(list):
        return 0
    return list[0] + sum_recursion(list[1:])


def count(list):
    if not list:
        return 0
    return 1 + count(list[1:])


def find_max(list):
    if len(list) == 2:
        return list[0] if list[0] >= list[1] else list[1]
    return list[0] if list[0] >= find_max(list[1:]) else find_max(list[1:])


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(sum_for([1, 2, 3, 4]))
    print(sum_recursion([1, 2, 3, 4]))
    print(count([1, 2, 3, 4]))
    print(find_max([1, 2, 3, 4]))
    print(quick_sort([10, 5, 2, 3]))