from random import randint
def create_matrix(n, random_from = 1, random_to = 9):
    matrix = []
    for _ in range(n):
        arr_in = []
        for _ in range(n):
            arr_in.append(randint(random_from, random_to))
            matrix.append(arr_in)
    return matrix
def test_create_matrix():
    assert create_matrix