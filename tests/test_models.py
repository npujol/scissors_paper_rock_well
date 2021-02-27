import pytest
from hypothesis import assume, given
from hypothesis.strategies import text
from pydantic import ValidationError

from scissors_paper_rock_well.models import Input, Throw

# Input creation take only the following values : scissors, paper, rock, well
# If the value is not valid, a validation error is thrown
@given(text(max_size=10))
def test_invalid_input(a):
    valid_trows = [v.value for v in Throw]
    assume(a not in valid_trows)
    with pytest.raises(ValidationError):
        Input(throw=a)


# Input create an objet from the string : scissors
def test_input_scissors_valid():
    assert Input(throw="scissors")


# Input create an objet from the string : rock
def test_input_rock_valid():
    assert Input(throw="rock")


# Input create an objet from the string : paper
def test_input_paper_valid():
    assert Input(throw="paper")


# Input create an objet from the string : well
def test_input_well_valid():
    assert Input(throw="well")
