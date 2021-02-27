from random import choice
from .models import Input, Output, Result, Throw


# The rules for the cases of win, when the first value beats the second one.
# I included only the win's cases, because to know the loss's cases you only have
# to change the order of the values.
RULES_FIRST_WIN = {
    # (user's throw, computer's throw)
    (Throw.SCISSORS, Throw.PAPER),
    (Throw.PAPER, Throw.ROCK),
    (Throw.PAPER, Throw.WELL),
    (Throw.ROCK, Throw.SCISSORS),
    (Throw.WELL, Throw.ROCK),
    (Throw.WELL, Throw.SCISSORS),
}

# With two throws(one from the user and other from the computer) return a result
def match(a: Throw, b: Throw) -> Result:
    # There are only three possible outcomes:
    #  1. Equal throws get draw (Result 1)
    if a == b:
        return Result.DRAW
    #  2. Different throws
    #    2.1 If they are in the winning rules it gets win (Result 2)
    if (a, b) in RULES_FIRST_WIN:
        return Result.WIN
    #    2.2 If they are not in the winning rules it gets loss (Result 3)
    return Result.LOSS


# Get a random throw (the computer's throw) using the values of Throw
def random_throw() -> Throw:
    return choice([v for v in Throw])


# Given the user's throw, the function get the computer's throw
# and return the result for the play.
def play(input: Input) -> Output:
    throw = random_throw()
    return Output(computer_throw=throw, result=match(input.throw, throw))
