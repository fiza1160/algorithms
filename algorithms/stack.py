def is_correct_bracket_sequence(brackets: str) -> bool:
    """
    Checks that the obtained bracket sequence is correct.
    The sequence may consist of characters '(', ')', '[', ']', '{', '}'.
    >>> is_correct_bracket_sequence('()[]{}')
    True
    >>> is_correct_bracket_sequence('([{}])')
    True
    >>> is_correct_bracket_sequence('([]{}{[]})')
    True
    >>> is_correct_bracket_sequence('(()')
    False
    >>> is_correct_bracket_sequence('([)]')
    False
    """
    paired_brackets = {
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '[',
        '{': '}',
        '}': '{'
    }
    open_brackets = {'(', '[', '{'}

    stack = []

    for bracket in brackets:
        if bracket in open_brackets:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            if paired_brackets[bracket] != stack.pop():
                return False

    if len(stack) != 0:
        return False

    return True


def reverse_polish_notation(expression: str) -> float|int:
    """
    Returns the result of calculating an expression written in Reverse Polish notation.
    In an expression, numbers and characters must be separated by spaces.
    >>> reverse_polish_notation('8 2 5 * + 1 3 2 * + 4 - /')
    6.0
    >>> reverse_polish_notation('7 2 3 * -')
    1
    >>> reverse_polish_notation('3 10 15 - *')
    -15
    """

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '/': lambda x, y: x / y,
        '*': lambda x, y: x * y
    }
    expression = expression.split()
    stack = []

    for symbol in expression:
        if symbol.isnumeric():
            stack.append(int(symbol))
        elif symbol in operations:
            if len(stack) >= 2:
                operand_2 = stack.pop()
                operand_1 = stack.pop()

                stack.append(operations[symbol](operand_1, operand_2))
            else:
                raise ValueError
        else:
            raise ValueError

    return stack.pop()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
