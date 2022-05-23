from Mission import Mission

# Some hints:
# Convert a number in the string with str(n)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(Mission.replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(Mission.replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(Mission.replace_first([1])) == [1]
    assert list(Mission.replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")