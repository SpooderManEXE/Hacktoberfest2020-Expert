def parentheses_check(text):
    stack = []
    for char in text:
        if char in ('(', '{', '['):
            stack.append(char)
        elif char in (')', '}', ']'):
            if stack.pop() != '({['[')}]'.index(char)]:
                return False
    return True


if __name__ == '__main__':
    test_text = 'this({"1": (1, 1), (2, 3): [3, 3, 3]}) is valid'
    print('{}: {}'.format(test_text, parentheses_check(test_text)))
    test_text = 'this({"1": (1, 1)), (2, 3): [3, 3, 3]}) is invalid'
    print('{}: {}'.format(test_text, parentheses_check(test_text)))
