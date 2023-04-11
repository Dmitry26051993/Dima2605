from funcs.funcs_08 import avg, avg_geom, result_avg
def test_avg():
    res = avg(3, 3, 3)
    assert res == 3
def test_avg_geom():
    res = avg_geom(3, 3, 3)
    assert res == 3
def test_res():
    res = result_avg(3, 3, 3, mean_type=1)
    assert res == 3

def test_res1():
    res = result_avg(2, 2, 2, mean_type=0)
    assert res == 2