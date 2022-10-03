import pytest
from main import calculate_two


# tests = [(2, 4), (0, 2), (10, 12), (100, 102), (-10, -8)]

# @pytest.mark.parametrize('test_inp, result', tests)
# def test_addition(test_inp, result):
#     assert add_two(test_inp) == result

test_calc = [('2 * 2', 4), ('9 / 3', 3), ('9 + 7', 16), ('1000 - 200', 800)]

@pytest.mark.parametrize('test_inp, result', test_calc)
def test_calculation(test_inp, result):
    assert calculate_two(test_inp) == result


# def test_division_by_zero():
#     assert calculate_two ('1 / 0') == None

# tests = [(0, 1), (1, 2), (8, 9)]

# @pytest.mark.parametrize('inp, result', tests)
# def test_rfl(inp, result):
#     assert return_from_list(inp) == result

# def test_rfl_error():
#     with pytest.raises(IndexError):
#         return_from_list(100)

# @pytest.mark.xfail(raises=IndexError)
# def test_rfl_xfail():
#     return_from_list(100)

# tests = [((10, 5), 2), ((8, 2), 4), ((9, 3), 3)]

# @pytest.mark.parametrize('test_inp, result ', tests)
# def test_division(test_inp, result):
#     assert division (*test_inp) == result # убираются скобки

# def test_rfl_error():
#     with pytest.raises(ZeroDivisionError):
#         division (100, 0)

# @pytest.mark.xfail(raises = ZeroDivisionError)
# def test_division_xfail():
#     division (1, 0)