def is_palindrome_recursive(word, low_index, high_index):
    if not isinstance(word, str) or len(word) <= 0:
        return False

    if len(word) > 100:
        raise RecursionError

    reversed_word = ''.join(list(reversed(word)))
    return True if reversed_word == word else False
