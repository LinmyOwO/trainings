from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(stmt, setup_code, repeat=3, number=8)

    # Return minimum time because it's likely the clearest time
    # (has the least amount of system "noise")
    return min(times)


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # swap
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array


def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        key_item = array[i]

        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array


def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] < right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_left == len(left):
            result.extend(right[index_right:])
            break
        if index_right == len(right):
            result.extend(left[index_left:])
            break

    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])
    )


def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort(array, i, min((i + min_run + 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), n - 1)

            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1]
            )

            array[start:start + len(merged_array)] = merged_array
        size *= 2

    return array


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 9999
    # Also add sorted case and reverse-sorted one
    arr = [randint(0, 10000) for i in range(ARRAY_LENGTH)]
    sorted_arr = sorted(arr)
    reverse_sorted_arr = sorted_arr[::-1]

    algorithms = (
        # "bubble_sort",
        # "insertion_sort",
        "merge_sort",
        "quicksort",
        "timsort",
        "sorted"
    )
    results = {}

    for algorithm in algorithms:
        print(f"Measuring {algorithm}...")
        # time for sorted, unsorted and sorted in reverse cases
        best, avg, worst = (
            run_sorting_algorithm(algorithm, sorted_arr),
            run_sorting_algorithm(algorithm, arr),
            run_sorting_algorithm(algorithm, reverse_sorted_arr)
        )
        results[algorithm] = {
            "sorted array": best,
            "unsorted array": avg,
            "reverse-sorted array": worst
        }

    print()
    algo_column_length = max([len(elem) for elem in algorithms])
    rsa_column_length = len("Reverse-sorted array")

    # the genius crutch for beautifulness cause I'm lazy
    print(f"Algorithm{(algo_column_length - 9) * ' '} | "
          f"Sorted array{(rsa_column_length - 12) * ' '} | "
          f"Unsorted array{(rsa_column_length - 14) * ' '} | "
          f"Reverse-sorted array")

    for algorithm, times in results.items():
        best, avg, worst = (
            times["sorted array"],
            times["unsorted array"],
            times["reverse-sorted array"]
        )

        best_time_padding = (len("Reverse-sorted array") - len(str(best))) * ' '
        avg_time_padding = (len("Reverse-sorted array") - len(str(avg))) * ' '

        padding = (algo_column_length - len(algorithm)) * ' '
        print(f"{algorithm}{padding} | {best}{best_time_padding}"
              f" | {avg}{avg_time_padding} | {worst}")
