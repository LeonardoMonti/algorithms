def partition(el, start, end):
    pivot = el[end]
    delimiter = start - 1

    for index in range(start, end):
        if el[index] <= pivot:
            delimiter = delimiter + 1
            el[index], el[delimiter] = (
                el[delimiter],
                el[index],
            )

    el[delimiter + 1], el[end] = el[end], el[delimiter + 1]

    return delimiter + 1


def quick_sort(el, start, end):
    if start < end:
        p = partition(el, start, end)
        quick_sort(el, start, p - 1)
        quick_sort(el, p + 1, end)
    return el


def is_anagram(first_string, second_string):
    first_lower = list(first_string.lower())
    second_lower = list(second_string.lower())

    quick_sort(first_lower, 0, len(first_lower) - 1)
    quick_sort(second_lower, 0, len(second_lower) - 1)

    first_sorted = "".join(first_lower)
    second_sorted = "".join(second_lower)

    if first_sorted == "" or second_sorted == "":
        return (first_sorted, second_sorted, False)
    elif first_sorted == second_sorted:
        return (first_sorted, second_sorted, True)
    else:
        return (first_sorted, second_sorted, False)
