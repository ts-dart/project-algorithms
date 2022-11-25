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

    for i in range(1, len(sort_str)):
        key_item = sort_str[i]
        j = i - 1

        while j >= 0 and sort_str[j] > key_item:
            sort_str[j + 1] = sort_str[j]
            j -= 1

        sort_str[j + 1] = key_item

    return ''.join(sort_str)


# print(is_anagram('muro', 'rumo'))
