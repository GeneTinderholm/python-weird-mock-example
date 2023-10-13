import pytest
import file1
from unittest.mock import patch


@pytest.fixture
def do_other_thing_with_mock():
    with patch.object(file1, "do_thing") as m:
        m.return_value = "hello world"
        import file2
        yield file2.do_other_thing


def test_do_other_thing(do_other_thing_with_mock):
    do_other_thing_with_mock()
