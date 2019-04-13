from .submodule import to_uppercase

def test_to_uppercase():
	assert to_uppercase('bagels') == 'BAGELS'