from pydantic import BaseModel
from typing import Optional, Union


class WordRequest(BaseModel):
    input: str
    word_count: Optional[int]

class SuccessResponse(BaseModel):
    response_code: int
    response_message: str
    output: Optional[str]
    
class ErrorResponse(BaseModel):
    response_code: int
    response_message: str  

response = Union[SuccessResponse, ErrorResponse]
