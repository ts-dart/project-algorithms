def is_anagram(first_string, second_string):
    ...

    first = my_sort(first_string.lower())
    second = my_sort(second_string.lower())
    result = (first, second, True)

    if len(first) == 0 or len(second) == 0:
        result = (first, second, False)

    if len(first) == len(second):
        for char in range(len(first)):
            if first[char] != second[char]:
                result = (first, second, False)
                break
    else:
        result = (first, second, False)

    return result


def my_sort(string):
    ...

    sort_str = list(string)

    for i in range(len(sort_str)):
        already_sorted = True
        for j in range(len(sort_str) - i - 1):
            if sort_str[j] > sort_str[j + 1]:
                sort_str[j], sort_str[j + 1] = sort_str[j + 1], sort_str[j]
                already_sorted = False

        if already_sorted:
            break
    return ''.join(sort_str)


# print(is_anagram('muro', 'rumo'))
