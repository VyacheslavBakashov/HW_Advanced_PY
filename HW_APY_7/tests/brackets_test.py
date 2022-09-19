from hw_apy_7 import is_balance
import pytest

test_list = [
    ('(((([{}]))))', 'Сбалансированно'),
    ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
    ('{{[()]}}', 'Сбалансированно'),
    ('}{}', 'Несбалансированно'),
    ('{{[(])]}}', 'Несбалансированно'),
    ('[[{())}]', 'Несбалансированно'),
]


@pytest.mark.parametrize('brackets_str, expected_res', test_list)
def test_is_balance(brackets_str, expected_res):
    assert is_balance(brackets_str) == expected_res
