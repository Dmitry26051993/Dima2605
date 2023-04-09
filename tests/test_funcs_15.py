def polindrom(my_str):
    my_str1 = my_str[::-1]
    if my_str == my_str1:
        print("Палиндром")
    else:
        print("Не палиндром")
def test_polindrom():
    assert polindrom
