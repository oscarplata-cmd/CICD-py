from print import print_data

def test_string():
    assert print_data("HOLA") == "HOLA"

def test_int():
    assert print_data(123) == "123"

