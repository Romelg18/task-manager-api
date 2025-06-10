from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from typing import Optional

class BaseTask(ABC):
    @abstractmethod
    def to_dict(self):
        pass

class Task(BaseModel):
    id: Optional[str] = Field(default=None)
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
