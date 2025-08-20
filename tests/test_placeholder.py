from src.main import hello

def test_math_is_still_trustworthy():
    assert 1 + 1 == 2

def test_hello_function_is_at_least_polite():
    assert "Welcome" in hello()
