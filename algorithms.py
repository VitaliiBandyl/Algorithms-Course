def my_reverse(array: list):
    """Invert array(functions reverse())"""
    n = len(array)
    for k in range(len(array) // 2):
        array[k], array[n - k - 1] = array[n - k - 1], array[k]
        print(array)


def test_my_reverse():
    A1 = [1, 2, 3, 4, 5]
    my_reverse(A1)
    inverted_A1 = [5, 4, 3, 2, 1]
    assert A1 == inverted_A1, f"Test 1 failed expected result{inverted_A1}, \n actual result {A1}"

    A2 = [0]
    my_reverse(A2)
    reversed_A2 = [0]
    assert A2 == reversed_A2, f"Test 2 failed expected result{reversed_A2}, \n actual result {A2}"

    A3 = [0, 0, 0, 0, 1]
    my_reverse(A3)
    reversed_A3 = [1, 0, 0, 0, 0]
    assert A3 == reversed_A3, f"Test 3 failed expected result{reversed_A3}, \n actual result {A3}"


test_my_reverse()
