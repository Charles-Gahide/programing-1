import time
time.sleep(10)
import pytest
import student

@pytest.mark.parametrize("number, name, type, expected_result", [
    (1, "Bulbasaur", "Grass-Poison", 'Pokemon(1, "Bulbasaur", "Grass-Poison")'),
    (4, "Charmander", "Fire", 'Pokemon(4, "Charmander", "Fire")'),
    (7, "Squirtle", "Water", 'Pokemon(7, "Squirtle", "Water")')
])
def test_pokemon_repr(number, name, type, expected_result):
    pokemon = student.Pokemon(number, name, type)

    assert repr(pokemon) == expected_result