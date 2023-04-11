from funcs.funcs_04 import create_matrix
res = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
def test_create_matrix():
   result = create_matrix(3)
   assert len(result) == len(res)
   assert len(result[0]) == 3