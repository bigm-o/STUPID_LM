from fastapi import FastAPI

app = FastAPI()
from src.predict import generate_sentence


from fastapi import FastAPI
from pydantic import BaseModel

from src.request_response import *

app = FastAPI()

def word_len(input):
        input_word_count = len(input.split())
        return input_word_count



#endpoint
@app.post("/predict_words", response_model=response)
def predict_words(request:WordRequest):

    request_dict = request.model_dump()
    input = request_dict["input"]
    word_count = request_dict["word_count"]

    print(word_len(input))
    print(word_count)

    if word_count <= 1 & word_len(input) >= 5:
        response_code = 401
        response_message = "Error: Word count too small"

    elif word_count <= 1 & word_len(input) < 5:
        response_code = 501
        response_message = "Error: Number of input words too small, and Word count too small"
    
    else:
        output = generate_sentence(input, word_count)
        response_code = 200
        response_message = "success"

        return SuccessResponse(
            response_code = response_code,
            response_message = response_message,
            output = output
        )

    return ErrorResponse(
        response_code = response_code,
        response_message = response_message
    )