from hypothesis import assume, given
from hypothesis.strategies import sampled_from

from scissors_paper_rock_well.core import match, play, random_throw
from scissors_paper_rock_well.models import Result, Throw, Output, Input

# Check if the computer's throw is a valid Throw
def test_random_throw():
    assert isinstance(random_throw(), Throw)


# Check if the play get a valid Output
def test_play_get_a_valid_output():
    scissors = Input(throw="scissors")
    assert isinstance(play(scissors), Output)


# Check if there is a result for all the possible couple of throws
@given(sampled_from(Throw), sampled_from(Throw))
def test_get_always_a_solution(a, b):
    assert isinstance(match(a, b), Result)


# Check if there is a result for the couple (a, b), but also for (b, a)
@given(sampled_from(Throw), sampled_from(Throw))
def test_asymmetry(a, b):
    assume(a != b)
    assert {match(a, b), match(b, a)} == {Result.LOSS, Result.WIN}


# Check if the result for the couple (a, a) is always draw.
@given(sampled_from(Throw))
def test_equal_throws(a):
    assert match(a, a) == Result.DRAW


# ---------------------------------------------------------------------
#                  CHECK SPECIFIC RULES
# ---------------------------------------------------------------------


# Check if for the couple scissors-paper, "match"  get the correct results
def test_scissors_beats_paper():
    assert match(Throw.SCISSORS, Throw.PAPER) == Result.WIN


# Check if for the couple paper-scissors, "match"  get the correct results
def test_paper_loses_scissors():
    assert match(Throw.PAPER, Throw.SCISSORS) == Result.LOSS


# -----------------------------------------------------------------------

# Check if for the couple paper-rock, "match"  get the correct results
def test_paper_beats_rock():
    assert match(Throw.PAPER, Throw.ROCK) == Result.WIN


# Check if for the couple rock-paper, "match"  get the correct results
def test_rock_loses_paper():
    assert match(Throw.ROCK, Throw.PAPER) == Result.LOSS


# -----------------------------------------------------------------------

# Check if for the couple paper-well, "match"  get the correct results
def test_paper_beats_well():
    assert match(Throw.PAPER, Throw.WELL) == Result.WIN


# Check if for the couple well-paper, "match"  get the correct results
def test_well_loses_paper():
    assert match(Throw.WELL, Throw.PAPER) == Result.LOSS


# -----------------------------------------------------------------------


# Check if for the couple rock-scissors, "match"  get the correct result
def test_rock_beats_scissors():
    assert match(Throw.ROCK, Throw.SCISSORS) == Result.WIN


# Check if for the couple scissors-rock, "match"  get the correct results
def test_scissors_loses_rock():
    assert match(Throw.SCISSORS, Throw.ROCK) == Result.LOSS


# -----------------------------------------------------------------------


# Check if for the couple well-rock, "match"  get the correct result
def test_well_beats_rock():
    assert match(Throw.WELL, Throw.ROCK) == Result.WIN


# Check if for the couple rock-well, "match"  get the correct results
def test_rock_loses_well():
    assert match(Throw.ROCK, Throw.WELL) == Result.LOSS


# -----------------------------------------------------------------------

# Check if for the couple well-scissors, "match"  get the correct result
def test_well_beats_scissors():
    assert match(Throw.WELL, Throw.SCISSORS) == Result.WIN


# Check if for the couple scissors-well, "match"  get the correct results
def test_well_loses_paper():
    assert match(Throw.SCISSORS, Throw.WELL) == Result.LOSS
