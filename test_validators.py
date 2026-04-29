
from validators import is_valid_email, is_valid_name, is_valid_phone



#Name Validation Tests
def test_is_valid_name():
    assert is_valid_name("John Smith") is True

def test_is_valid_name_with_space():
    assert is_valid_name("John Doe") is True


def test_invalid_name_empty():
    assert is_valid_name("") is False

def test_invalid_name_numbers():
    assert is_valid_name("John123") is False


#Email Validation Tests
def test_is_valid_email():
    assert is_valid_email("john@example.com") is True

def test_invalid_email_format():
    assert is_valid_email("john@example") is False

def test_invalid_email_no_at():
    assert is_valid_email("johnexample.com") is False

#Phone Validation Tests
def test_is_valid_phone():
    assert is_valid_phone("1234567890") is True

def test_invalid_phone_letters():
    assert is_valid_phone("12345abcde") is False

def test_invalid_phone_short():
    assert is_valid_phone("12345") is False

def test_invalid_phone_long():
    assert is_valid_phone("123456789012345") is False

def test_invalid_phone_special_characters():
    assert is_valid_phone("123-456-7890") is False

def test_invalid_phone_empty():
    assert is_valid_phone("") is False

def test_valid_phone_min_length():
    assert is_valid_phone("1234567890") is True
