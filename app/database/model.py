from typing import Optional
import uuid
from pydantic import (
    BaseModel,
    Field
)

class Item(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str
    description: Optional[str]
    
class UpdateItem(BaseModel):
    name: Optional[str]
    description: Optional[str]