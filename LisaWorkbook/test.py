from main import workbook

def test_workbook():
    assert workbook(5, 3, [4, 2, 6, 1, 10]) == 4
    assert workbook(10, 5, [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]) == 8