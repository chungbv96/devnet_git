import pytest


# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def test_task_stdout(capsys):
    """
    Task check
    """
    import task_6_1

    out, err = capsys.readouterr()
    correct_stdout = "['aabb.cc80.7000', 'aabb.dd80.7340', 'aabb.ee80.7000', 'aabb.ff80.7000']"
    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        correct_stdout in out.strip()
    ), "Wrong line is printed to stdout"


def test_task_variables():
    """
    Проверка что в задании создана нужная переменная
    и в ней содержится правильный результат
    """
    import task_6_1

    # переменные созданные в задании:
    task_vars = [var for var in dir(task_6_1) if not var.startswith("_")]

    correct_result = ['aabb.cc80.7000', 'aabb.dd80.7340', 'aabb.ee80.7000', 'aabb.ff80.7000']

    assert (
        "result" in task_vars
    ), "Итоговый список должен быть записан в переменную result"
    assert (
        type(task_6_1.result) == list
    ), f"По заданию в переменной result должен быть список, а в ней {type(task_6_1.result).__name__}"
    assert (
        task_6_1.result == correct_result
    ), f"В переменной result должен быть список {correct_result}"


