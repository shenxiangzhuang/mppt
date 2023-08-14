from ppt_package.hello import hello


def test_hello() -> None:
    msg = hello()
    assert isinstance(msg, str)
