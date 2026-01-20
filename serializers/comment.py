from pydantic import BaseModel


class CommentSchema(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True


class CreateCommentSchema(BaseModel):
    name: str
    content: str

    class Config:
        orm_mode = True


class UpdateCommentSchema(BaseModel):
    name: str
    content: str

    class Config:
        orm_mode = True
