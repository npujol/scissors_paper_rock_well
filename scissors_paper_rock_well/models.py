from enum import Enum
from pydantic import BaseModel

# The possible throw values (scissors, paper, rock, well)
class Throw(Enum):
    SCISSORS = "scissors"
    ROCK = "rock"
    PAPER = "paper"
    WELL = "well"


# The possible result values (win, loss, draw)
class Result(Enum):
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
