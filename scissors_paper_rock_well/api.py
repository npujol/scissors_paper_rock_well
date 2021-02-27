from fastapi import FastAPI
from scissors_paper_rock_well.models import Input, Output

app = FastAPI()


# Create a endpoint to post a play
def create_play(input: Input) -> Output:
    pass