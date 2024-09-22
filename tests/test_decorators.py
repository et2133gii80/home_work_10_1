from typing import Any

from src.decorators import log


@log()
def test_function_success(x: Any, y: Any) -> Any:
    return x + y


@log()
def test_function_error(x: Any, y: Any) -> Any:
    raise ValueError("Function error")


def test_log_success(capsys: Any) -> Any:
    test_function_success(1, 2)

    captured = capsys.readouterr()
    assert captured.out == "test_function_success ok\n"


def test_log_error(capsys: Any) -> Any:
    test_function_error(1, 2)

    captured = capsys.readouterr()
    assert "test_function_error error: ValueError. Inputs: (1, 2), {}\n" in captured.out


def test_log_to_file(tmpdir: Any) -> Any:
    log_file = tmpdir.join("test_log.txt")

    @log(filename=str(log_file))
    def test_function_file_success(x: Any, y: Any) -> Any:
        return x + y

    @log(filename=str(log_file))
    def test_function_file_error(x: Any, y: Any) -> Any:
        raise ValueError("Function error")

    test_function_file_success(1, 2)

    with open(str(log_file), "r") as f:
        log_content = f.read()

    assert "test_function_file_success ok" in log_content

    test_function_file_error(1, 2)

    with open(str(log_file), "r") as f:
        log_content = f.read()

    assert "test_function_file_error error: ValueError. Inputs: (1, 2), {}" in log_content
