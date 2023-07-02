from main import serviceLane

def test_servicelane():
    width = [2, 3, 1, 2, 3, 2, 3, 3]
    cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
    expected_result = [1, 2, 3, 2, 1]
    assert serviceLane(width, cases) == expected_result

    width = [1, 2, 2, 2, 1]
    cases = [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]]
    expected_result = [2, 1, 1, 1, 2]
    assert serviceLane(width, cases) == expected_result