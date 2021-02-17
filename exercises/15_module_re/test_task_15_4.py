import pytest
import task_15_4
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_function_created():
    """
    Проверка, что функция создана
    """
    check_function_exists(task_15_4, "get_ints_without_description")


def test_function_return_value():
    """
    Проверка работы функции
    """
    correct_return_value = [
        "Loopback0",
        "Tunnel0",
        "Ethernet0/1",
        "Ethernet0/3.100",
        "Ethernet1/0",
    ]
    return_value = task_15_4.get_ints_without_description("config_r1.txt")
    assert return_value != None, "Функция ничего не возвращает"
    assert (
        type(return_value) == list
    ), f"По заданию функция должна возвращать список, а возвращает {type(return_value).__name__}"
    assert sorted(return_value) == sorted(
        correct_return_value
    ), "Функция возвращает неправильное значение"
