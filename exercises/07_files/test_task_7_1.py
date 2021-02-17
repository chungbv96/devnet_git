import re
from functools import wraps
import pytest
import sys

sys.path.append("..")
from pyneng_common_functions import strip_empty_lines

# Checking that the test is called via pytest ... and not python ...
from _pytest.assertion.rewrite import AssertionRewritingHook

if not isinstance(__loader__, AssertionRewritingHook):
    print(f"Tests should be called using this expression:\npytest {__file__}\n\n")


def unified_columns_output(output):
    output = strip_empty_lines(output)
    lines = [re.split(r"  +", line.strip()) for line in output.strip().split("\n")]
    formatted = [("{:25}"*len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


def test_task(capsys):
    """
    Task check при вводе access
    """
    import task_7_1

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Prefix                    10.0.24.0/24\n"
        "AD/Metric                 110/41\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d18h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.28.0/24\n"
        "AD/Metric                 110/31\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d20h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.37.0/24\n"
        "AD/Metric                 110/11\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d20h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.41.0/24\n"
        "AD/Metric                 110/51\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d20h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.78.0/24\n"
        "AD/Metric                 110/21\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d20h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.79.0/24\n"
        "AD/Metric                 110/20\n"
        "Next-Hop                  10.0.19.9\n"
        "Last update               4d02h\n"
        "Outbound Interface        FastEthernet0/2\n"
    )

    assert (
        out
    ), "Nothing is printed to stdout. It is necessary not only to get the correct result, but also to print it to the stdout using printprint"
    assert (
        unified_columns_output(out.strip()) == correct_stdout
    ), "На стандартный поток вывода выводится неправильный вывод"

