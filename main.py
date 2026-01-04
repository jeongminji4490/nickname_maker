from fastapi import FastAPI
from models.nickname import NicknameRequest, NicknameResponse
from services.nickname_ai import generate_nickname

app = FastAPI()

@app.post("/nickname", response_model=NicknameResponse)
def recommend_nickname(input: NicknameRequest):
    gpt_result = generate_nickname(input.model_dump())
    
    return {
        "input": input,
        "categories": gpt_result["categories"]
    }

