from enum import Enum
from pydantic import BaseModel

# The possible throw values (scissors, paper, rock, well)
# Inherit from srt, so that the fastapi documentation shows the Enum values.
class Throw(str, Enum):
    SCISSORS = "scissors"
    ROCK = "rock"
    PAPER = "paper"
    WELL = "well"


# The possible result values (win, loss, draw)
# Inherit from srt, so that the fastapi documentation shows the Enum values.
class Result(str, Enum):
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"


# A Throw object(user entry)
class Input(BaseModel):
    throw: Throw


# A Throw object(the computer throw) and a Result
class Output(BaseModel):
    computer_throw: Throw
    result: Result
