from fastapi import FastAPI
from .models import Input, Output
from .core import play

app = FastAPI(
    title="scissors_paper_rock_well",
    description='A version of the game scissor-paper-rock, but including a new word "well".',
    version="0.1.0",
    docs_url="/",
)


# Create a endpoint to post a play
@app.post("/play/", response_model=Output)
async def create_play(input: Input) -> Output:
    return play(input)
