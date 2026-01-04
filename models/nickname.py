from pydantic import BaseModel

class NicknameRequest(BaseModel):
    name: str
    age: int
    gender: str
    vibe: str

class NickName(BaseModel):
    name: str
    description: str

class NicknameCategory(BaseModel):
    nicknames: list[NickName]
    theme: str

class NicknameResponse(BaseModel):
    input: NicknameRequest
    categories: list[NicknameCategory]