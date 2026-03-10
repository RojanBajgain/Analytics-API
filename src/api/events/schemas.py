from typing import List, Optional
from pydantic import BaseModel, Field


class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str] = Field(default="My Description")


class EventUpdateSchema(BaseModel):
    description: Optional[str] = Field(default="My Description")


class EventSchema(BaseModel):
    id: int
    page: Optional[str] = ""
    description: Optional[str] = ""


class EventListSchema(BaseModel):
    items: List[EventSchema]
    count: int
