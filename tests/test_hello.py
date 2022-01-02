# tests/test_main.py
from mylib import hello


def test_main() -> None:
    result = hello.main()
    assert result == "Hello..."
