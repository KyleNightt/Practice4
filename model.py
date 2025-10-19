from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Make music"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {"item": "Nasyrov"},
                    {"item": "IVT-430B"}
                ]
            }
        }