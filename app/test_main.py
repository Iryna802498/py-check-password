import pytest


from app.main import check_password


@pytest.mark.parametrize("password, result", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("1234567", False),
    ("12345678901234567", False),
    ("P@ssword1998", False),
    ("NoDigits!", False),
    ("N0Specials", False),
    ("nocapital1@", False),
    ("ValidPass1!", True),
])
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
